@echo off

rem author: laplaciannin102
echo _________________________________________________________________________________________
echo author: laplaciannin102
echo.
echo this bat file let you pip install from files.
echo _________________________________________________________________________________________
echo.

rem change current directory
cd /d %~dp0

set py_pkgs_files_dpath=python_pkgs_files

echo list of files in %py_pkgs_files_dpath%
echo.

echo ^>^>call dir ^/b %py_pkgs_files_dpath%
echo ========================================
call dir /b %py_pkgs_files_dpath%
echo ========================================

echo.

set input_pkgs_fname=
set /p input_pkgs_fname=select a packages file name : 

set input_pkgs_fpath=%py_pkgs_files_dpath%/%input_pkgs_fname%

echo.
echo ========================================
echo pip install from %input_pkgs_fpath% is start.
echo ========================================
echo.

echo.
echo Do you want to install it as a user??
echo (pip install --user package)
set user_install=
set /p user_install=Yes or No??(y/n) : 

if %user_install%==y (
    set user_install=Yes
)
if %user_install%==n (
    set user_install=No
)

echo.

rem pip install command
set pip_install_cmd=pip install

rem user install mode
if %user_install%==Yes (
    set pip_install_cmd=pip install --user
    echo user install start.
    echo.
)

if %user_install%==No (
    echo not user install start.
    echo.
)


rem run pip install line by line from the file
for /f %%l in (%input_pkgs_fpath%) do (

    rem pip install
    echo ========================================
    echo ^>^>call %pip_install_cmd% "%%l"
    echo ========================================
    echo.

    call %pip_install_cmd% "%%l"

    echo.
    echo _________________________________________________________________________________________
    echo.

)

echo ========================================
echo pip install from %input_pkgs_fpath% is end.
echo ========================================
echo.

pause
