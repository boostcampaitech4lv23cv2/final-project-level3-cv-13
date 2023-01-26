#dockerhub image settings
FROM python:3.8.15-slim

COPY . .
ENV GOOGLE_APPLICATION_CREDENTIALS="google_key.json"

RUN pip install pip==22.3.1 && \
    pip install -r backend/requirements.txt

ENTRYPOINT  ["streamlit", "run", "frontend/simple_streamlit_web.py","--server.fileWatcherType=none", "--server.address=0.0.0.0", "--server.port=443"]
EXPOSE 443