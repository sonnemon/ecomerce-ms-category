FROM python:3.7.10-slim-buster
WORKDIR /usr/app
COPY . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["pymon", "src/app.py"]
