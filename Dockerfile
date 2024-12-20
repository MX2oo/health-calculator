FROM python:3.9-slim

RUN apt update && apt    install -y curl

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python3", "app.py"]
