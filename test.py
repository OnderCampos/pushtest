# data_analysis.py

# Importing standard libraries
import json
import csv
import re
import logging

# Importing third-party libraries
import seaborn as sns
import scipy.stats as stats
import sqlalchemy as db

# Importing specific functions from a module
from collections import defaultdict, Counter
from itertools import combinations, permutations

# Importing a module from a package
from flask import Flask, request, jsonify

# Printing to check if the imports work correctly
print("All imports are successful!")
