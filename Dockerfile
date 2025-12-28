FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

# App files
WORKDIR /Ghost-Forward-Bot
COPY . .

# Start bot
CMD ["python", "main.py"]
