@echo off

rem author: laplaciannin102
echo _________________________________________________________________________________________
echo author: laplaciannin102
echo.
echo this bat file let you conda install from files.
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
echo conda install from %input_pkgs_fpath% is start.
echo ========================================
echo.

rem run conda install line by line from the file 
for /f %%l in (%input_pkgs_fpath%) do (

    rem conda install
    echo ========================================
    echo ^>^>echo y^|call conda install "%%l"
    echo ========================================
    echo.

    echo y|call conda install "%%l"

    echo.
    echo _________________________________________________________________________________________
    echo.

)

echo ========================================
echo conda install from %input_pkgs_fpath% is end.
echo ========================================
echo.

pause
