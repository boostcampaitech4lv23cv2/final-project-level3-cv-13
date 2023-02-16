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
from airflow.providers.google.cloud.operators.gcs import GCSDeleteObjectsOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.utils.trigger_rule import TriggerRule

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
PROJECT_ID = os.environ.get("SYSTEM_TESTS_GCP_PROJECT")
DAG_ID = "gcs_to_sftp"

SFTP_CONN_ID = "aistages"
BUCKET_NAME = "user-data-cv13"
DESTINATION_PATH_FISH = "/opt/ml/data2/fish"
DESTINATION_PATH_SASHIMI = "/opt/ml/data2/sashimi"
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

    fish_image_delete = GCSDeleteObjectsOperator(
            task_id="fish-image-delete",
            bucket_name='ficv_dataset',
            prefix='fish/'
    )
    
    sashimi_image_delete = GCSDeleteObjectsOperator(
            task_id="sashimi-image-delete",
            bucket_name='ficv_dataset',
            prefix='sashimi/'
    )

    (
        fish_image_delete >> sashimi_image_delete
    )
