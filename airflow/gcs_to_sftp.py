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
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule

ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
PROJECT_ID = os.environ.get("SYSTEM_TESTS_GCP_PROJECT")
DAG_ID = "gcs_to_sftp"

SFTP_CONN_ID = "aistages"
BUCKET_NAME = "user-data-cv13"
DESTINATION_PATH_FISH = "/opt/ml/af_test/fish"
DESTINATION_PATH_SASHIMI = "/opt/ml/af_test/sashimi"
GCS_FISH_DIR = "fish/*"
GCS_SASHIMI_DIR = "sashimi/*"
date = "{{ ds_nodash }}"

with models.DAG(
    DAG_ID,
    schedule="@once",
    start_date=datetime(2023, 2, 5),
    catchup=False,
    tags=["example", "gcs"],
) as dag:

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

    # filename_label_score   
    # rename
    (
        move_dir_fish >> move_dir_sashimi
    )