# Airflow

> Airflow 서버를 gcp에서 구동시키고 다른 계정의 gcp bucket과 aistages 서버에 연결하여 이미지를 옮길 수 있도록 설정하였습니다.

### GCP 준비
- https://medium.com/apache-airflow/a-simple-guide-to-start-using-apache-airflow-2-on-google-cloud-1811c2127445
- https://ruuci.tistory.com/6

### Docker compose를 이용하여 Airflow 설치
- https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
- https://mep997.tistory.com/27

### Google Cloud Connection
- Connection Id = "원하는 이름"
- Connection Type = Google Cloud
- Keyfile Path = gcp에 업로드 해 놓은 keyfile 절대경로
    - ex) /opt/airflow/dags/key.json
    - 주의!) keyfile path, keyfile json, keyfile secret name은 중복하여 작성X
- key file을 생성한 서비스 계정의 권한은 storage object admin으로 설정해야 파일에 접근할 수 있다.

### SFTP server Connection
- Connection Id = "원하는 이름"
- Connection Type = SFTP
- Host = 연결할 서버의 IP 주소
- username = 서버의 username
- Port = sftp port 번호
- Extra = gcp에 업로드 해 놓은 ssh keyfile의 위치를 json 형식으로 입력
    - ex) {"key_file": "/opt/airflow/dags/key}
- 참고자료: https://docs.aws.amazon.com/ko_kr/mwaa/latest/userguide/samples-ssh.html

### Dag 작성
- gcs to sftp: https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/transfer/gcs_to_sftp.html
- execute bash command on sftp server: https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/operators/ssh/index.html