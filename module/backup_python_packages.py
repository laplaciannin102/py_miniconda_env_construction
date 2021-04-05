#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: laplaciannin102
@date: 20xx/xx/xx
@version: 0.0.1
@history:
    20xx/xx/xx:
        初期版作成.
"""



# --------------------------------------------------------------------------------
# Load modules
# --------------------------------------------------------------------------------

import numpy as np
import pandas as pd

# original modules
from pycfg import *



# --------------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------------

def read_txt_file(file_path):
    with open(file_path, mode='r') as f:
        txt = f.read()
    return txt


def read_lines_txt_file(file_path):
    with open(file_path, mode='r') as f:
        lines = f.readlines()
    return lines


def write_txt_file(file_path, txt):
    with open(file_path, mode='w') as f:
        f.write(txt)


def convert_conda_list(line, eq_txt='>='):
    ret = line
    if not '# ' in line:
        splitted_line = line.split('=')
        
        if len(splitted_line) >= 2:
            # ret = '{}>={}\n'.format(splitted_line[0], splitted_line[1])
            ret = '{}{}{}'.format(
                splitted_line[0],
                eq_txt,
                splitted_line[1]
            )
    return ret



# --------------------------------------------------------------------------------
# conda
# --------------------------------------------------------------------------------

print('convert conda packages files.')
print()

conda_is_success = False

try:

    # read
    # conda_list_txt0 = read_txt_file(conda_list_file0)
    conda_list_txt0 = read_lines_txt_file(conda_list_file0)


    # eq
    # convert
    conda_list_eq_txt = '\n'.join([convert_conda_list(line, eq_txt='==') for line in conda_list_txt0 if not '#' in line])

    # write
    write_txt_file(conda_list_eq_file, conda_list_eq_txt)


    # geq
    # convert
    conda_list_geq_txt = '\n'.join([convert_conda_list(line, eq_txt='>=') for line in conda_list_txt0 if not '#' in line])

    # write
    write_txt_file(conda_list_geq_file, conda_list_geq_txt)
    
    conda_is_success = True

except Exception as e:
    
    print('error: convert conda packages files.')
    print(e)



# --------------------------------------------------------------------------------
# pip
# --------------------------------------------------------------------------------

print('convert pip packages files.')
print()

pip_is_success = False

try:
    
    # read
    pip_list_txt0 = read_txt_file(pip_list_file0)


    # geq
    # convert
    pip_list_eq_txt = pip_list_txt0

    # write
    write_txt_file(pip_list_eq_file, pip_list_eq_txt)


    # geq
    # convert
    pip_list_geq_txt = pip_list_txt0.replace('==', '>=')

    # write
    write_txt_file(pip_list_geq_file, pip_list_geq_txt)
    
    pip_is_success = True

except Exception as e:
    
    print('error: convert pip packages files.')
    print(e)



# --------------------------------------------------------------------------------
# get preinstall anaconda packages list
# --------------------------------------------------------------------------------

print('get preinstall anaconda packages list file.')
print()

print('anaconda_packages_url:')
print(anaconda_packages_url)
print()

preinstall_is_success = False

try:
    
    # anaconda packages dataframe
    anaconda_packages_table = pd.read_html(anaconda_packages_url)
    anaconda_packages_df = anaconda_packages_table[0]

    anaconda_packages_df.columns = [
        'name',
        'version',
        'summary_license',
        'in_installer'
    ]

    print('anaconda_packages_df.shape: {}'.format(anaconda_packages_df.shape))
    print()
    print('*' * 80)
    print('anaconda_packages_df:')
    print()
    print(anaconda_packages_df.head(3))
    print('*' * 80)
    print(anaconda_packages_df.tail(3))
    print('*' * 80)

    # get list
    anaconda_preinstall_list = anaconda_packages_df.apply(
        lambda x: '{}=={}'.format(
            x['name'],
            x['version']
        ),
        axis=1
    ).values.tolist()

    # eq
    # convert
    anaconda_preinstall_list_eq_txt = '\n'.join(anaconda_preinstall_list)

    # write
    write_txt_file(
        anaconda_preinstall_list_eq_file,
        anaconda_preinstall_list_eq_txt
    )
    
    preinstall_is_success = True

except Exception as e:
    
    print('error: convert pip packages files.')
    print(e)



# --------------------------------------------------------------------------------
# Check
# --------------------------------------------------------------------------------

print()

print('*' * 80)
print('output file names:')
print()

if conda_is_success:
    print('conda_list_file0: {}'.format(conda_list_file0))
    print('conda_list_eq_file: {}'.format(conda_list_eq_file))
    print('conda_list_geq_file: {}'.format(conda_list_geq_file))

    print()

if pip_is_success:
    print('pip_list_file0: {}'.format(pip_list_file0))
    print('pip_list_eq_file: {}'.format(pip_list_eq_file))
    print('pip_list_geq_file: {}'.format(pip_list_geq_file))

    print()

if preinstall_is_success:
    print('anaconda_preinstall_list_eq_file: {}'.format(anaconda_preinstall_list_eq_file))

print('*' * 80)

print()

print('convert packages files finish.')
