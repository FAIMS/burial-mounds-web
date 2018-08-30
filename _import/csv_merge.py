#!/usr/bin/env python3
"""Module that merge two csv on a key and output a new csv."""
import argparse
import pandas as pd

PARSER = argparse.ArgumentParser(
    description='A program that takes two csv and merge the two csv with the \
    column name passed as the key. It returns a new csv with supplied name')
PARSER.add_argument('-k', '--key', help='Key to merge on')
PARSER.add_argument('-o', '--output', help='Name of output file')
PARSER.add_argument('-f', '--first', help='Name of first file')
PARSER.add_argument('-s', '--second', help='Name of second file')

# To take a list
# PARSER.add_argument('-n', '--names-list', nargs='+', default=[])

ARGS = vars(PARSER.parse_args())

KEY = ARGS['key']
OUTPUT = ARGS['output']
FIRST = ARGS['first']
SECOND = ARGS['second']

FIRST_CSV = pd.read_csv(FIRST)
SECOND_CSV = pd.read_csv(SECOND)

SECOND_CSV = SECOND_CSV.dropna(axis=1)

print(FIRST_CSV.head())
print(SECOND_CSV.head())

# Sanitize KEY, replace space with '_' and make it key lowercase
#KEY = KEY.replace(' ','_').lower()

MERGED = FIRST_CSV.merge(SECOND_CSV, on=KEY)
print(MERGED.head())
MERGED.to_csv(OUTPUT, index=False)
