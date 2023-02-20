FROM python:3.9.16-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Обновляем пакетный менеджер
RUN apt-get update -y && apt-get upgrade -y

# Ставим зависимости GDAL, PROJ
RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# COPY ./entrypoint.sh .
# RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
# RUN chmod +x /usr/src/app/entrypoint.sh

# COPY . .

# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
