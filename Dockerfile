FROM python:3.8.2-buster
RUN mkdir /src
ADD . /src
RUN cd /src \
	&& make install
WORKDIR /usr/local/bin
ENTRYPOINT ["/usr/local/bin/promotiond"]
CMD ["--help"]
