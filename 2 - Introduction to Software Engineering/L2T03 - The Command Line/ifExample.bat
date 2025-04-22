@echo off
# Verifies new folders
if exist "new_folder" (
    mkdir if_folder
)

REM Makes the folder on condition
if exist "if_folder" (
    mkdir hyperionDev
) else (
    mkdir new-projects
)