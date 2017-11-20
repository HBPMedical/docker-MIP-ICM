FROM hbpmip/python-mip:0.1.3

MAINTAINER clementine.fourrier@icm-institute.org

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="hbpmip/icm-algorithm" \
      org.label-schema.description="Executes the ICM algorithm" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vendor="ICM" \
      org.label-schema.schema-version="1.0"

ARG LOGIN
ARG PASSWORD

RUN echo "deb http://deb.debian.org/debian stretch main" >> /etc/apt/sources.list
RUN echo "deb-src http://deb.debian.org/debian stretch main" >> /etc/apt/sources.list

# Installing the basics (gcc, g++, ...)
RUN rm var/lib/apt/lists/httpredir.debian.org_debian_dists_jessie_main_binary-amd64_Packages.gz
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y \
build-essential \
cmake \
git

# Installing armadillo
RUN apt-get install -y libopenblas-dev
RUN apt-get install -y liblapack-dev #libopenlapack to check and use instead
RUN apt-get install -y libarmadillo-dev

# Installing python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pandas

# Installing Longitudina
RUN git clone https://$LOGIN:$PASSWORD@gitlab.icm-institute.org/aramislab/longitudina -b HBP longitudina
RUN cd longitudina/ && rm -rf build && \
git submodule init && git submodule update && \
cmake . && make

COPY utils/utils.py utils/utils.py
COPY utils/utils_highcharts.py utils/utils_highcharts.py
COPY utils/utils_inputs.py utils/utils_inputs.py
COPY utils/utils_PFA.py utils/utils_PFA.py
COPY algo.py /main.py
COPY main_univariate.sh /main_univariate.sh
COPY main_multivariate.sh /main_multivariate.sh
#CMD ["./main.py"]