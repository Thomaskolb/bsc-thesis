# Thomas Kolb s1027332
# This program interprets all the collected results from training and creates tensorboard log

import tensorflow as tf
import sys

# Number of datapoints per configuration
dps_per_config = 3

# Write data dictionary to tensorflow log file
def write_data(data, outpath):
    for config in data:
        file_writer = tf.summary.create_file_writer(f'{outpath}/{config}')
        with file_writer.as_default():
            for i in range(len(data[config])):
                print(i)
                print(data[config])
                tf.summary.scalar('results', data[config][i], step=i)
    # ASR data
    file_writer = tf.summary.create_file_writer(f'{outpath}/asr-results')
    with file_writer.as_default():
        tf.summary.scalar('results', 0.31011388388465866, step=0)
        tf.summary.scalar('results', 0.31011388388465866, step=1)
        tf.summary.scalar('results', 0.31011388388465866, step=2)

# Interpret data given from differen configuration outputs
def interpret_data(config_path_list):
    data_dict = {}
    config_id = 1
    dataset_id = 0
    for config_path in config_path_list:
        with open(config_path, 'r') as file:
            print(config_path)
            number = (file.read().split('\n')[-3]).split(' ')[-1]
            value = float(number)
            if f'configuration {config_id}' not in data_dict:
                data_dict[f'configuration {config_id}'] = [value]
            else:
                data_dict[f'configuration {config_id}'].append(value)
        dataset_id = (dataset_id + 1) % dps_per_config
        if dataset_id == 0:
            config_id += 1
    return data_dict

if len(sys.argv) < 3:
    print("Please enter the output path and the configuration data paths")
else:
    write_data(interpret_data(sys.argv[2:]), sys.argv[1])