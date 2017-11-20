#!/usr/bin/env python3

import logging
import os
#import sys
import math


def get_parameters_from_population_file(path):
    return

def get_parameters_from_individual_file(path):
    return

def get_model_function(type):
    return

# TODO: convert to PFA, with inputs t0 and v0
def get_univariate_function(t, p, v0, t0):
    """
    Univariate function
    Args:
        t (float): Timescore (equivalent to x)
        p (float):
        v0 (float): acceleration of the slope (individual parameter)
        t0 (float): initial start of the slope for the specific individual (individual parameter)
        p0 = 1/(1 + math.exp(-p))
        result = 1/(1+(1/p0 - 1)*math.exp(-v0*(t-t0)))
    """
    return {"input":
                {
                "type": "record",
                "fields":{
                        {"name": "t", "type": float},
                        {"name": "p", "type": float},
                        {"name": "v0", "type": float},
                        {"name": "t0", "type": float}
                    }
                },
            "output": "float",
            "action":
                {"/":
                    [1,
                    {"+":
                       [1,
                        {"*":
                            [{"+":
                                [{"/":
                                    [1,
                                    {"/":
                                        [1,
                                        {"+":
                                            [1,
                                            {"m.exp": [{"u-": [input.p]}]}]
                                         }]
                                    }] #P0 end
                                },
                                {"u-": [1]}]
                            },
                            {"m.exp":
                                [{"*", [{"u-": [input.v0]},
                                        {"-" : [input.t,
                                                input.t0]}]
                                }]
                            }]
                        }]
                    }]
                }
            }

# TODO: convert to PFA, with inputs t0 and v0
def get_multivariate_function(t, g, delta, w, v0, t0):
    """
    Multivariate function
    Args:
        t (float): Timescore (equivalent to x)
        g (float)
        delta (float):
        w (float): weight
        v0 (float): acceleration of the slope (individual parameter)
        t0 (float): initial start of the slope for the specific individual (individual parameter)
        equation: 1 / (1 + g*math.exp ((-w*math.pow(g*math.exp(-delta)+1,2)/g*math.exp(-delta)) - delta - v0*(t - t0)) )
        """
    return {"input":
                {
                "type": "record",
                "fields":{
                        {"name": "t", "type": float},
                        {"name": "g", "type": float},
                        {"name": "w", "type": float},
                        {"name": "v0", "type": float},
                        {"name": "t0", "type": float},
                        {"name": "delta", "type": float}
                    }
                },
            "output": "float",
            "action":
                { "/",
                    [1,
                    {"+",
                        [1,
                        {"*",
                            [input.g,
                            {"m.exp",
                                [{"+",
                                    [{"*",
                                        [{"*",
                                            [{"u-", [input.w]},
                                             {"m.exp", [{"u-", [input.delta]}]}]
                                          },
                                        {"/",
                                            [{"**",
                                                [{"+",
                                                    [{"*", [input.g,
                                                            {"m.exp", [{"u-", [input.delta]}]}]
                                                      },
                                                      1]
                                                  },
                                                  2]
                                              },
                                              input.g]
                                        }]
                                    },
                                    {"+",
                                        [{"u-", [input.delta]},
                                         {"*",
                                            [{"u-", [input.v0]},
                                             {"-", [input.t, input.t0]}]
                                         }]
                                    }]
                                }]
                            }]
                        }]
                    }]
                }
            }

def write_output_to_highchart(model_type):
    #reads the population file
    #creates the pfa file
    #creates the dict for the population
    #creates the dict for the individuals
    return

# Might need to add a transformation function to go from the dictionnary to lists to write in the different files,
# especially if we get several queries.
def write_input_to_file(data):
    path_to_group_file = "examples/scalar_models/univariate/data/groups.csv"
    path_to_X_file = "examples/scalar_models/univariate/data/X.csv"
    path_to_Y_file = "examples/scalar_models/univariate/data/Y.csv"

    data_stores = data["data"]["independent"]
    dimension = 1
    for item_dict in data_stores:
        if item_dict["name"] == "id":
            write_content_to_file(item_dict["series"], path_to_group_file)
        if item_dict["name"] == "age":
            write_content_to_file(item_dict["series"], path_to_X_file)
        if item_dict["name"] == "scores":
            write_content_to_file(item_dict["series"], path_to_Y_file)
            dimension = item_dict["series"].size()

    model_type = edit_settings_files(dimension)

    return model_type

# If needed, edit this function to use several series (for multivariate).
def write_content_to_file(serie, path_to_file):
    file = open(path_to_file, "w+")
    for value in serie:
        file.write(value)
    file.close()


# This function must edit the settings file to take into account the number of scores (the dimension)
# and return the model_type
def edit_settings_files(dimension):
    # write dimension in xml

    model_type = ""
    if dimension == 1:
        model_type = "univariate"
    elif dimension > 1:
        model_type = "multivariate"
    return model_type