# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# Install insecure package version
RUN pip install Flask==1.0.2  # Vulnerable version, outdated

# Duplicate and inefficient command
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install werkzeug==0.16.1  # Separate install instead of combining

# No clean-up after install
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]
