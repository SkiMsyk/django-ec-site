FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /vegeket
COPY vegeket/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY /vegeket/ .
