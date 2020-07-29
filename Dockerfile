FROM python:3.6

RUN pip install Flask

RUN pip install pytest 

RUN pip install pylint

RUN pip install flake8

WORKDIR /home

