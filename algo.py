#!/usr/bin/env python3

import logging
import os
import sys
sys.path.append("/Users/clementine.fourrier/Documents/Projets/HBP/python-base-docker-images/python-mip/io_helper/io_helper/")
import io_helper
from utils import utils


def main():
    logging.basicConfig(level=logging.INFO)
    data = io_helper.fetch_data() #renverra des dataframes pandas => 2 novembre, envoyer message to Mirco
    print(data)
    print("End of the dataaaaa")
    model_type = utils.write_input_to_file(data)
    os.system("./main_" + model_type + ".sh")
    highchart = utils.write_output_to_highchart(model_type)
    print(highchart)
    error = 0
    shape = 0
    io_helper.save_results(highchart, error, shape)





if __name__ == '__main__':
    main()
