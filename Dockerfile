### Create container with the volume in the same path
### More information: https://rest-apis-flask.teclado.com/docs/docker_intro/
### docker run -dp 5000:5000  -w /app  -v "$(pwd):/app"  flask-smorest-api
FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
