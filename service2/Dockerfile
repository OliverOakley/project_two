FROM python:3.7
WORKDIR /service2
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5002
ENTRYPOINT ["python", "app.py"]