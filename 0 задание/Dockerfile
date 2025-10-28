FROM python:3.15-nonexistent-tag

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir totally-fake-package==0.0.0

EXPOSE 5000

CMD ["python", "main.py"]
