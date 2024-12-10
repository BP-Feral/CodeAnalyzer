import re
import tkinter as tk
from tkinter import filedialog


def preprocess_code(code):
    code_no_comments = re.sub(r'#.*', '', code)  # Python comments (single and block)
    code_no_strings = re.sub(r'(\'[^\']*\'|"[^"]*")', '', code_no_comments) # Strings (single and double quotes)
    return code_no_strings

def find_unused_variables(code):
    code_cleaned = preprocess_code(code)
    declared = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b(?=\s*=)', code_cleaned)
    used = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b(?!\s*=)(?!\s*\()', code_cleaned)
    
    unused = set(declared) - set(used)
    return list(unused)

def remove_css_duplicates(css):
    lines = css.splitlines()
    seen = set()
    unique_lines = []

    for line in lines:
        # Remove whitespace and ignore empty lines
        line = line.strip()
        if not line:
            continue

        property_name = line.split(":")[0].strip() # Split property and value
        
        if property_name not in seen: # Collect unique properites
            seen.add(property_name)
            unique_lines.append(line)

    return "\n".join(unique_lines)


def extract_comments(code):
    pattern = r"(#.*?$|//.*?$|/\*.*?\*/)"
    matches = re.findall(pattern, code, re.DOTALL | re.MULTILINE)
    return matches