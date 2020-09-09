import os, sys
import yaml

class ReadData(object):
    # / Users / panda / Desktop / app_test / data / data.yaml
    def __init__(self, filename):
        self.file_path = os.getcwd() + os.sep + "data" + os.sep + filename

    def return_data(self):
        with open(self.file_path, 'r') as f:

            return  yaml.load(f)


