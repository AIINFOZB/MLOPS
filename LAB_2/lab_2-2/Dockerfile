FROM python:3.9
COPY . /apps/

WORKDIR /apps
RUN python -m pip install --upgrade pip
CMD ["bash", "pipeline.sh"]
