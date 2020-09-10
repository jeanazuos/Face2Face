FROM python:3.6-slim-stretch

MAINTAINER Jean Souza <jean.azuos@gmail.com>

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

COPY app.py /app/
COPY cli /app/cli
COPY controller /app/controller
COPY model /app/model
COPY views /app/views
COPY static /app/static
COPY requirements.txt /app/

WORKDIR /app

ENV ALLOWED_EXTENSIONS "{'png', 'jpg', 'jpeg', 'gif'}"
ENV MAX_CONTENT_LENGTH "16777216"
ENV CLI_MAIN_PATH_CHECK "TESTE_DE_BIOMETRIA_FACIAL"
ENV CLI_DEFAULT_IMAGE_NAME_ONE "Imagem_1.JPG"
ENV CLI_DEFAULT_IMAGE_NAME_TWO "Imagem_2.JPG"

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]