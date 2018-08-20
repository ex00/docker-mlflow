# AUTHOR: ex00
# DESCRIPTION: mlflow container
# BUILD: docker build --rm -t ex00/docker-mlflow .
# SOURCE: https://github.com/ex00/docker-mlflow


FROM continuumio/miniconda3:latest
MAINTAINER ex00

RUN pip install --upgrade pip 
RUN pip install mlflow

RUN conda install pytorch-cpu torchvision-cpu -c pytorch && \ 
    conda install tensorflow keras -c conda-forge


COPY ./examples /examples

CMD mlflow ui --host 0.0.0.0