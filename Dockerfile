FROM python:3.7-alpine

COPY src /app
RUN python3 /app/main.js
