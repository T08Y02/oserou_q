FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
   apt-get -y install sudo gcc nano vim lsof net-tools
RUN mkdir /oserou_q
WORKDIR /oserou_q
ADD ./oserou_q/oserou_q/requirements.txt /oserou_q/
RUN pip install -r requirements.txt
ADD ./oserou_q /oserou_q