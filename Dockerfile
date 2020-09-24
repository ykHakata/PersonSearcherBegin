FROM perl:5.14.4
RUN cpanm Carton && mkdir -p /usr/src/app
WORKDIR /usr/src/app
