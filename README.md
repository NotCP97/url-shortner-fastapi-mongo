# URL shorter using FastAPI and mongodb

## Description

A URL shortener using FastAPI, Streamlit and mongodb.

## Features

- Shorten URL
- Redirect to original URL

## Installation

Instructions on how to install the project, for example:

```bash
git clone https://github.com/NotCP97/url-shortner-fastapi-mongo.git
cd projectname
pip install -r requirements.txt
```
create a .env file and add the following   
MONGO_DETAILS=your_mongo_url

## Running the project

Backend server run
```bash
uvicorn main:app --reload
```
Stream lit UI run
```bash
streamlit run ui.py
```

## Future Work
<s>write basic ui for the project </s>  
different folder and Dockerfile for backend and UI  
Use redis for count to remove count from mongodb collection  
write docker-compose file for the project


