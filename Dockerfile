FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3 python3-pip
WORKDIR /app/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "packt.py"]