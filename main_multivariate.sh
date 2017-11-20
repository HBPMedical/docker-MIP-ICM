#!/usr/bin/env bash

cd longitudina/
exec build/Longitudina fit \
examples/scalar_models/multivariate/settings/model_settings.xml \
examples/scalar_models/multivariate/settings/algorithm_settings.xml \
examples/scalar_models/multivariate/settings/data_settings.xml \
examples/scalar_models/multivariate/settings/sampler_settings.xml \
0
echo "done"
cd outputs/
ls