FROM python:3.9.2-buster

COPY main.py /app/
WORKDIR /app/

ENTRYPOINT ["python3", "main.py"]
