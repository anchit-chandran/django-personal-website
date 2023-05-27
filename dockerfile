FROM python:3.10-slim-buster

WORKDIR /app

# COPY REQUIREMENTS TEXT INTO CONTAINER
COPY requirements.txt requirements.txt

# INSTALL DEPENDENCIES
RUN pip3 install -r requirements.txt

# COPY ENTIRE CONTENTS OF FOLDER INTO CONTAINER
COPY . .

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]

