@echo off

rem change current directory
cd /d %~dp0

set py_fpath=./backup_python_packages.py

rem echo ^>^>call python %py_fpath%
call python %py_fpath%
