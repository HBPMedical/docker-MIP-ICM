FROM icm-base-docker:latest #hbpmip/python-mip:0.1.3

MAINTAINER clementine.fourrier@icm-institute.org

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="hbpmip/icm-algorithm" \
      org.label-schema.description="Executes the ICM algorithm" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vendor="ICM" \
      org.label-schema.schema-version="1.0"

ARG LOGIN
ARG PASSWORD

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