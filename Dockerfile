FROM ubuntu:20.04
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt install iputils-ping -y
RUN apt install iproute2 -y
RUN apt install net-tools -y
RUN apt install apt-utils -y
RUN apt install postgresql-contrib curl -y
RUN apt install python3-distutils-extra python3-dev unixodbc-dev -y
RUN apt install libpq-dev -y