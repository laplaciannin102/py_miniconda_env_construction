@echo off

rem author: laplaciannin102
echo _________________________________________________________________________________________
echo author: laplaciannin102
echo.
echo this bat file backs up python packages,
echo and gets ready to move python environment.
echo _________________________________________________________________________________________
echo.

rem change current directory
cd /d %~dp0

set py_pkgs_files_dpath=python_pkgs_files

echo make directory for packages files
echo ^>^>call mkdir %py_pkgs_files_dpath%
call mkdir %py_pkgs_files_dpath%

echo _________________________________________________________________________________________
echo.

echo command1 to avoid conda errors
echo ^>^>echo y^|call conda install anaconda
echo y|call conda install anaconda

echo _________________________________________________________________________________________
echo.

echo command2 to avoid conda errors
echo ^>^>echo y^|call conda update ^-^-all
echo y|call conda update --all

echo _________________________________________________________________________________________
echo.

set conda_list_file0=%py_pkgs_files_dpath%/conda_pkgs_list_raw.txt

echo output conda packages file

rem echo ^>^>call conda list > %conda_list_file0%
rem call conda list > %conda_list_file0%

rem echo ^>^>call conda list ^-^-export ^-^-no-pip ^> %conda_list_file0%
rem call conda list --export --no-pip > %conda_list_file0%

echo ^>^>call conda list ^-^-export ^> %conda_list_file0%
call conda list --export > %conda_list_file0%

echo _________________________________________________________________________________________
echo.

set pip_list_file0=%py_pkgs_files_dpath%/pip_pkgs_list_raw.txt

echo output pip packages file

rem use pip freeze
rem echo ^>^>call pip freeze ^> %pip_list_file0%
rem call pip freeze > %pip_list_file0%

rem use pip list
echo ^>^>call pip list ^-^-format freeze ^> %pip_list_file0%
call pip list --format freeze > %pip_list_file0%


rem setlocal enabledelayedexpansion
rem for /f "delims=" %%a in (%pip_list_file0%) do (
rem set line=%%a
rem echo !line:%eq_string%=%geq_string%!>>%pip_list_file1%
rem )

echo _________________________________________________________________________________________
echo.

set exe_bat_fpath=./module/execute_py_module.bat

echo ^>^>call %exe_bat_fpath%
call %exe_bat_fpath%

echo _________________________________________________________________________________________
echo.

echo ready to move environment.

pause
