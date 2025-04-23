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
    match_list = []
    
    for line in line_list:
        # print(f"{line}") # it can go thru all lines. line var considered a string

        pattern = r"^(.*?)\s\|\s(\w+)\s\|\s(\w+)\s\|\s(.*)$"
        match = re.match(pattern, line) #this tries to match each entire line
        
        if match: #this part modified from ChatGPT
           match_list.append(match.groups()) 

def count_log_levels(parsed):
    count_dict = {"INFO": {}, "WARNING":{}, "ERROR":{}, "CRITICAL":{}}

    for tuple in parsed:
        level = tuple[2]
        message = tuple[3]
        count_i, count_e, count_w, count_l = 0

        if level == "INFO":
            count_dict["INFO"][message] = count_i + 1
        elif level == "ERROR":
            count_dict["ERROR"][message] = count_e + 1
        elif level == "WARNING":
            count_dict["WARNING"][message] = count_w + 1
        elif level == "CRITICAL":
            count_dict["CRITICAL"][message] = count_l + 1
