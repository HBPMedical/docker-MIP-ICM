#!/usr/bin/env bash

cd longitudina/
exec build/Longitudina fit \
examples/scalar_models/univariate/settings/model_settings.xml \
examples/scalar_models/univariate/settings/algorithm_settings.xml \
examples/scalar_models/univariate/settings/data_settings.xml \
examples/scalar_models/univariate/settings/sampler_settings.xml \
0
echo "done"
cd outputs/
ls