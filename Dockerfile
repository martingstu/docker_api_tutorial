FROM python:3.7-slim

#Make a directory for our app
WORKDIR /usr/src/app

#Install whatever dependencies are required
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#Copy all the contents from the folder/workspace to directory in the container
COPY . .

#Run the app!!!
ENTRYPOINT ["python"]
CMD ["app.py"]