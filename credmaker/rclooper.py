#!/usr/bin/env python3
import csv

f = open("csv_users.txt","r")
i = 0 

for row in csv.reader(f):
    i = i +1;

