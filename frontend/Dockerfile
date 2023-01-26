#dockerhub image settings
FROM python:3.8.15-slim

COPY . .

RUN pip install pip==22.3.1 && \
    pip install -r frontend/requirements.txt

ENTRYPOINT  ["streamlit", "run", "frontend/simple_streamlit_web.py","--server.fileWatcherType=none", "--server.port","443","--server.address","0.0.0.0","--browser.gatherUsageStats","False"]
EXPOSE 443