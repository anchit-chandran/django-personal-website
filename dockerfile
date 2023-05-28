FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY ./requirements.txt .

# INSTALL DEPENDENCIES
RUN pip3 install -r requirements.txt

# COPY ENTIRE CONTENTS OF FOLDER INTO CONTAINER
COPY . .

# RUN SETUP COMMANDS
CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]
