@echo off
""" This batch file demonstrates how to create folders, navigate into them, and remove subfolders using the command line in Windows. """
# Create three folders on the Desktop
mkdir folder1 folder2 folder3

# Navigate to the Desktop
cd folder1

# Create three subfolders in folder1
mkdir subfolder1 subfolder2 subfolder3

# Removes two subfolders
rmdir /q subfolder1 
rmdir /q subfolder2

# Returns to the Desktop
cd ..
