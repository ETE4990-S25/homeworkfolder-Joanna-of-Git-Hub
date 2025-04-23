# Paste your python file here don't for get to upload it with your submission
import re

def read_log_line(log_filepath):
    # structure taken from Mr. Power's Lecture 6 notes
    try: 
        with open(log_filepath, "r") as file:
            lines = file.readlines()
        return lines
    except:
        FileNotFoundError

def parse_log_line(line_list):
    for line in line_list:
        # print(f"{line}") # it can go thru all lines. line var considered a string

        pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
        match = re.match(pattern, line) #this tries to match each entire line
        
        if match: #this section modified from ChatGPT
           return match.groups()


def count_log_levels(line):
    a = 1
