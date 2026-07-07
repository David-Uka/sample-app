FROM python:3.13-alpine
WORKDIR /app
COPY app.py .
USER 1000
EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s CMD wget -qO- http://localhost:8080/healthz || exit 1
CMD ["python", "app.py"]
