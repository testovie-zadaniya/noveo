FROM ubuntu:latest
MAINTAINER Sergey Scherbakov "flare@flare.ws"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /server
WORKDIR /server
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-u", "client.py"]

