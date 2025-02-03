FROM python:3.13.1-slim
WORKDIR /app

#Install application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#bring everything into the container
COPY . .

#expose port for Flask
EXPOSE 5000

#start the application
CMD ["python", "calculator.py"]
