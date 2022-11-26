FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY resturant.py ./
COPY dishes.txt ./

CMD ["python3", "./resturant.py"]



