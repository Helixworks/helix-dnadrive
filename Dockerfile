FROM python:2.7
MAINTAINER Wingston Sharon "wingston@helix.works"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN mkdir -p /tmp/flaskfiles/
EXPOSE 5000
CMD ["python","server.py"]
