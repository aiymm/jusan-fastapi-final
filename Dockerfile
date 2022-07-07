FROM python:latest
RUN pip3 install fastapi uvicorn prometheus_client
EXPOSE 8080
COPY main.py /
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]


