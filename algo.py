#!/usr/bin/env python3

import logging
import os
import sys
sys.path.append("/Users/clementine.fourrier/Documents/Projets/HBP/python-base-docker-images/python-mip/io_helper/io_helper/")
import io_helper
import utils


def main():
    logging.basicConfig(level=logging.INFO)
    data = io_helper.fetch_data() #renverra des dataframes pandas => 2 novembre, envoyer message to Mirco
    print("This is the dataaaaa")
    print(data)
    print("End of the dataaaaa")
    #utils.write_input_to_file(data)
    os.system("./main.sh")
    pfa = utils.write_output_to_pfa("Multivariate")
    print pfa
    error = 0
    shape = 0
    io_helper.save_results(pfa, error, shape)





if __name__ == '__main__':
    main()
