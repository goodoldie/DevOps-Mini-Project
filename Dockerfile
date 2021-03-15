FROM python:3.8-buster
WORKDIR /app
COPY calcy_main.py .
COPY requirements.txt .
COPY scientific_calculator.py .
RUN pip3 install -r requirements.txt

#File will be run from here onwards
ENTRYPOINT python3 calcy_main.py
