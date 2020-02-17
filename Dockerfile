# build stage
FROM python:3.8.1-alpine as grpcio
RUN apk update \
    && apk add --no-cache ca-certificates \
    && update-ca-certificates \
    && pip install --upgrade pip wheel
RUN apk --no-cache add build-base linux-headers
RUN set -ex \
    && wget -O grpcio.tar.gz "https://files.pythonhosted.org/packages/74/52/9204d08bf37ac2505ebab2fa93b808fac87564580d7cc839db2fe11c3bdd/grpcio-1.27.2.tar.gz" \
    && mkdir -p /usr/src/grpcio \
	&& tar -zxC /usr/src/grpcio --strip-components=1 -f grpcio.tar.gz \
	&& rm grpcio.tar.gz \
    && cd /usr/src/grpcio \
    && python setup.py bdist_wheel

# build stage
FROM python:3.8.1-alpine as tools
RUN apk update \
	&& apk add --no-cache ca-certificates \
	&& update-ca-certificates \
	&& pip install --upgrade pip wheel
RUN apk --no-cache add build-base linux-headers
RUN set -ex \
	&& wget -O grpcio-tools.tar.gz "https://files.pythonhosted.org/packages/34/81/08f956aab9a2f28ea01e29c1935a67f48627a595bdc78c2a401467ae06c0/grpcio-tools-1.27.2.tar.gz" \
	&& mkdir -p /usr/src/grpcio-tools \
	&& tar -zxC /usr/src/grpcio-tools --strip-components=1 -f grpcio-tools.tar.gz \
	&& rm grpcio-tools.tar.gz \
	&& cd /usr/src/grpcio-tools \
    && python setup.py bdist_wheel

# final stage
FROM python:3.8.1-alpine
RUN apk update \
	&& apk add --no-cache ca-certificates build-base postgresql-dev \
	&& update-ca-certificates \
	&& pip install --upgrade pip
RUN mkdir /src
COPY --from=grpcio /usr/src/grpcio/dist/grpcio-1.27.2-cp38-cp38-linux_x86_64.whl /src
COPY --from=tools /usr/src/grpcio-tools/dist/grpcio_tools-1.27.2-cp38-cp38-linux_x86_64.whl /src
ADD . /src
RUN cd /src \
	&& pip install grpcio-1.27.2-cp38-cp38-linux_x86_64.whl \
	&& pip install grpcio_tools-1.27.2-cp38-cp38-linux_x86_64.whl \
	&& make install
WORKDIR /usr/local/bin
ENTRYPOINT ["/usr/local/bin/promotiond"]
CMD ["--help"]
