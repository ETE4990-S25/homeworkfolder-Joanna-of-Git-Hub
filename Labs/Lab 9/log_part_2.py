import re
import ast

def read_log_line(log_filepath):
    # structure taken from Mr. Power's Lecture 6 notes
    with open(log_filepath, "r") as file:
        lines = ast.literal_eval(file.readlines())

def parse_log_line(line):
    pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
    match = re.match(pattern, line)