FROM python:3.7.11-stretch

WORKDIR /usr/src/app

RUN apt-get update --allow-unauthenticated -y

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy necessary files
COPY recommender_app recommender_app
COPY app.py app.py

CMD [ "streamlit", "run", "app.py" ]
