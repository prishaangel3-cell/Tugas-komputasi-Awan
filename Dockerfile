FROM python:3.10-slim
WORKDIR /app

RUN echo "Hello from Docker!" > index.html
EXPOSE 80

CMD ["python3", "-m", "http.server", "80"]
