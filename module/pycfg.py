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

from datetime import datetime



# --------------------------------------------------------------------------------
# Constants
# --------------------------------------------------------------------------------

# date
today_dt = datetime.today()
today_str = '{}{}{}'.format(
    str(today_dt.year).zfill(4),
    str(today_dt.month).zfill(2),
    str(today_dt.day).zfill(2)
)

# paths
# dir path
pkgs_dir_path = '../python_pkgs_files/'

# conda
conda_list_file0 = '{}conda_pkgs_list_raw.txt'.format(pkgs_dir_path)
conda_list_eq_file = '{}conda_pkgs_list_eq_{}.txt'.format(pkgs_dir_path, today_str)
conda_list_geq_file = '{}conda_pkgs_list_geq_{}.txt'.format(pkgs_dir_path, today_str)

# pip
pip_list_file0 = '{}pip_pkgs_list_raw.txt'.format(pkgs_dir_path)
pip_list_eq_file = '{}pip_pkgs_list_eq_{}.txt'.format(pkgs_dir_path, today_str)
pip_list_geq_file = '{}pip_pkgs_list_geq_{}.txt'.format(pkgs_dir_path, today_str)

# anaconda
anaconda_packages_url = 'https://docs.anaconda.com/anaconda/packages/py3.8_win-64/'
anaconda_preinstall_list_eq_file = '{}anaconda_preinstall_pkgs_list_eq_{}.txt'.format(pkgs_dir_path, today_str)

