FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3
RUN mkdir /home/app && cd /home/app
COPY calcy_main.py .
COPY requirements.txt .
COPY scientific_calculator.py .

#File will be run from here onwards
ENTRYPOINT python3 calcy_main.py
