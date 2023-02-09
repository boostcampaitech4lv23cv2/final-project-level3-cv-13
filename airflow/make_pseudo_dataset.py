#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example Airflow DAG for Google Cloud Storage to SFTP transfer operators.
"""
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

from airflow import models
from airflow.providers.google.cloud.transfers.gcs_to_sftp import GCSToSFTPOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.utils.trigger_rule import TriggerRule

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
PROJECT_ID = os.environ.get("SYSTEM_TESTS_GCP_PROJECT")
DAG_ID = "gcs_to_sftp"

SFTP_CONN_ID = "aistages"
BUCKET_NAME = "ficv_bucket"
DESTINATION_PATH_FISH = "/opt/ml/af_test/fish"
DESTINATION_PATH_SASHIMI = "/opt/ml/af_test/sashimi"
GCS_FISH_DIR = "fish/*"
GCS_SASHIMI_DIR = "sashimi/*"
date = "{{ ds_nodash }}"
sshHook = SSHHook(ssh_conn_id=SFTP_CONN_ID)

with models.DAG(
    DAG_ID,
    schedule="@once",
    start_date=datetime(2023, 2, 5),
    catchup=False,
    tags=["example", "gcs"],
) as dag:

    dummy = DummyOperator(
            task_id = "start",
    )
    
    # today folder name
    fish_mkdir_today = SSHOperator(
            task_id="fish-mkdir-today",
            command="mkdir -p {{params.fish_des}}/{{ ds_nodash }}",
            ssh_hook=sshHook,
            params={'fish_des': DESTINATION_PATH_FISH,
                    'date': date,
            }
    )

    sashimi_mkdir_today = SSHOperator(
            task_id="sashimi-mkdir-today",
            command="mkdir -p {{params.sashimi_des}}/{{ ds_nodash }}",
            ssh_hook=sshHook,
            params={'sashimi_des': DESTINATION_PATH_SASHIMI,
                    'date': date,
            }
    )


    # [START howto_operator_gcs_to_sftp_move_specific_files]
    move_dir_fish = GCSToSFTPOperator(
            task_id="fish-move-gsc-to-sftp",
            sftp_conn_id=SFTP_CONN_ID,
            source_bucket=BUCKET_NAME,
            source_object=GCS_FISH_DIR,
            destination_path=os.path.join(DESTINATION_PATH_FISH, date),
            keep_directory_structure=False,
    )

    move_dir_sashimi = GCSToSFTPOperator(
            task_id="sashimi-move-gsc-to-sftp",
            sftp_conn_id=SFTP_CONN_ID,
            source_bucket=BUCKET_NAME,
            source_object=GCS_SASHIMI_DIR,
            destination_path=os.path.join(DESTINATION_PATH_SASHIMI, date),
            keep_directory_structure=False,
    )
    
    make_dataset = SSHOperator(
            task_id="make-dataset",
            command="python /opt/ml/final-project-level3-cv-13/Data/utils/pseudo_dataset.py --date=\"{{ ds_nodash }}\"",
            ssh_hook=sshHook,
            params={'sashimi_des': DESTINATION_PATH_SASHIMI,
                    'date': date,
            }
    )

    (
        dummy >> fish_mkdir_today >> move_dir_fish >> make_dataset,
        dummy >> sashimi_mkdir_today >> move_dir_sashimi >> make_dataset
    )
