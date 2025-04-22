import re
import json

def read_log_line(log):
    # structure taken from Mr. Power's Lecture 6 notes
    with open(log, "r") as file:
        lines = file.readlines()

def parse_log_line(line):
    pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
    match = re.match(pattern, line)