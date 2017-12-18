FROM icm-base-docker

MAINTAINER clementine.fourrier@icm-institute.org

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="hbpmip/icm-algorithm" \
      org.label-schema.description="Executes the ICM algorithm" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vendor="ICM" \
      org.label-schema.schema-version="1.0"

# Installing Longitudina
RUN git clone https://oauth2:Qgqe3QnzXYAM7YsQTwd_@gitlab.icm-institute.org/aramislab/longitudina -b HBP dockerlongitudina
RUN cd longitudina/ && rm -rf build && \
git submodule init && git submodule update && \
cmake . && make

COPY utils/utils.py utils/utils.py
COPY utils/utils_highcharts.py utils/utils_highcharts.py
COPY utils/utils_inputs.py utils/utils_inputs.py
COPY utils/utils_PFA.py utils/utils_PFA.py
COPY main.py /main.py
COPY main_univariate.sh /main_univariate.sh
COPY main_multivariate.sh /main_multivariate.sh
#CMD ["./main.py"]