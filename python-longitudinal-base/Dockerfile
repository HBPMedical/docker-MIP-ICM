FROM hbpmip/python-mip:latest as python-longitudinal-base

MAINTAINER clementine.fourrier@icm-institute.org

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="icm-base-docker" \
      org.label-schema.description="Base docker" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vendor="ICM" \
      org.label-schema.schema-version="1.0"

RUN echo "deb http://deb.debian.org/debian stretch main" >> /etc/apt/sources.list
RUN echo "deb-src http://deb.debian.org/debian stretch main" >> /etc/apt/sources.list

# Installing the basics (gcc, g++, ...)
#RUN rm var/lib/apt/lists/httpredir.debian.org_debian_dists_jessie_main_binary-amd64_Packages.gz
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