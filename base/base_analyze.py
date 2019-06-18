import os

import yaml


def analyze_data(file_name, key):

    with open(".%sdata%s%s.yaml" % (os.sep, os.sep, file_name), "r") as f:
        case_data = yaml.load(f)[key]

        data_list = list()
        for i in case_data.values():
            data_list.append(i)

        return data_list
