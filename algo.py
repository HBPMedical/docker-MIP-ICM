#!/usr/bin/env python3

import logging
import os
import sys
sys.path.append("/Users/clementine.fourrier/Documents/Projets/HBP/python-base-docker-images/python-mip/io_helper/io_helper/")
try:
    import io_helper
except:
    print("No import")
from utils import utils


def main():
    logging.basicConfig(level=logging.INFO)
    try:
        data = io_helper.fetch_data() #renverra des dataframes pandas => 2 novembre, envoyer message to Mirco
        print(data)
        model_type = utils.write_input_to_file(data)
        print("End of the dataaaaa")
    except:
        model_type = "univariate"
    os.system("./main_" + model_type + ".sh")
    highchart = utils.write_output_to_highchart(model_type)
    print(highchart)
    io_helper.save_results(highchart, "application/highcharts+json")





if __name__ == '__main__':
    main()
