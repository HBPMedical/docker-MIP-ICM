#!/usr/bin/env python3

import logging
import os
#import sys
import math


def generate_data_univar(p0, v0, t0):
    loc_series = []
    for t in range(40, 110):
        loc_series.append({'x': t, 'y': 1. / (1. + (1./ p0 - 1) * math.exp(-v0*(t-t0)))})
    return loc_series

def generate_data_multivar():
    return

def generate_all_data_univar(pop_param, indiv_param):
    loc_series = []
    p0 = pop_param['p']
    v0 = math.exp(pop_param['ksimean'])
    t0 = pop_param['taumean']

    loc_series.append({'data': generate_data_univar(p0, v0, t0), 'name': 'Mean'})
    for id_patient in indiv_param.keys():
        print(indiv_param[id_patient])
        t0 = indiv_param[id_patient]['tau']
        v0 = math.exp(float(indiv_param[id_patient]['ksi']))
        id = indiv_param[id_patient]['id']
        indiv_results = generate_data_univar(p0, v0, t0, id);
        loc_series.append({'data': indiv_results, 'name': 'Patient ' + id});
    return loc_series


def read_population_parameters(path_to_file):
    """
    Reads the population parameters file
    Args:
        path_to_file: the path to the population file Longitudina outputted

    Returns:
        dict: a dictionnary with the name of the parameters as keys and their values as values
    """
    params = {}
    f = open(path_to_file, 'r')

    for line in f:
        line = line.lower()

        # Extract parameters
        list_elements = line.split()
        param_name = list_elements[0]
        param_values = [float(list_elements[i]) for i in range(1, len(list_elements))]

        # Add to existing dict
        params[param_name] = param_values[0] if len(param_values) == 1 else param_values

    f.close()

    return params


def read_individual_parameters(file_name):
    """
    Reads the individual parameters file
    Args:
        file_name: the path to the population file Longitudina outputted

    Returns:
        dict: a dictionnary with the name of the parameters as keys and their values as values
        dict: a dictionnary linking the ids and rids of the elements
    """
    f = open(file_name, 'r')

    # Get the parameters
    labels = f.readline().lower().split()
    number_per_label = f.readline().split()

    params = []
    for idx, name in enumerate(labels):
        params.append((name, int(number_per_label[idx])))

    # Get the parameters
    individual_parameters = {}
    for line in f:
        if line == "":
            continue

        list_elements = line.split()

        # Add individuals
        individual_parameters[list_elements[0]] = compute_individual_parameters(list_elements, params)

    return individual_parameters


def compute_individual_parameters(list_elements, number_of_params):
    """ Reads the individual parameters file
    Args:
        list_elements: the list of the lines extracted from the files
        number_of_params: the number of parameters per trajectory

    Returns:
        dict: dictionnary of individual parameters
    """
    individual_parameters = {}
    idx_start = 0

    for tpl in number_of_params:
        idx_end = idx_start + tpl[1]
        if tpl[0] == "id":
            individual_parameters[tpl[0].rstrip()] = [(list_elements[i].rstrip()) for i in range(idx_start, idx_end)]
        else:
            individual_parameters[tpl[0].rstrip()] = [float(list_elements[i].rstrip()) for i in range(idx_start, idx_end)]
        idx_start = idx_end

    return individual_parameters


def write_univar_output_to_highchart():
    pop_param = read_population_parameters("longitudina/examples/scalar_models/univariate/output/population_parameters.txt")
    indiv_param = read_individual_parameters("longitudina/examples/scalar_models/univariate/output/individual_parameters.txt")
    series = generate_all_data_univar(pop_param, indiv_param)
    result_string = "{title: {text: 'Evolution of scores in time'},yAxis: {title: {text: 'Scores'}}, xAxis: {title: " \
                    "{text: 'Age'}}, legend: {layout: 'vertical',align: 'right',verticalAlign: 'middle',borderWidth: 0}, " \
                    "series: " + series + "}"

    print(result_string)

    return result_string