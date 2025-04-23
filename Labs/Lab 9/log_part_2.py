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
        pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
        match = re.match(pattern, line)
        if match:
            timestamp, log_level, message = match.groups()
            print(f"Timestamp: {timestamp}, Level: {log_level}, Message: {message}")


def count_log_levels(line):
    a = 1
