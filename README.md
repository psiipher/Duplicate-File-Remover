# Duplicate-File-Remover
This script detects duplicate files by verifying checksum and can be used to delete them.

This script is written in pyhton3.

This scripts detects duplicate files in a given a directory path (absolute path should be provided).
It asks the user whether the duplicate file should be deleted or not.
It can be scheduled to run after a certain time interval provided by the user (should be provided in terms of minutes).
It uses MD5 hashing algorithm for generating checksum.

To run the script:
python3 main.py [OPTIONS] or [PATH]
 
OPTIONS:   -h help
           -u usage
  
PATH:       Absolute path of directory.
