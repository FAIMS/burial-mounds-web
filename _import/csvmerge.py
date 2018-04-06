#!/usr/bin/env python3

import csv
import os
import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='A program that takes two csv and merge the two csv with the column name passed a key. It returns a new csv with supplied name')
parser.add_argument('-k', '--key', help='Key to merge on')
parser.add_argument('-o', '--output', help='Name of output file')
parser.add_argument('-f', '--first', help='Name of first file')
parser.add_argument('-s', '--second', help='Name of second file')



# To take a list
# parser.add_argument('-n', '--names-list', nargs='+', default=[])


args = vars(parser.parse_args())

key = args['key']
output = args['output']
first = args['first']
second = args['second']

first_csv = pd.read_csv(first)
second_csv = pd.read_csv(second)

b = b.dropna(axis=1)

merged = first_csv.merge(second_csv, on=key)
merged.to_csv(output,index=False)
