# Ramiro Flores Villarreal
# A01710879
# 01 / 03 / 2024
# Implementation of Computational methods Project: Lexical Analysis E1
# Regular Expression

import regex

pattern = r'C(ALEN|ALMA|ARCA|ELEB|ERTAR)'

# Test strings
test_strings = [

# Matching Strings
    'CALEN', 
    'CALMA', 
    'CARCA',  
    'CELEB',  
    'CERTAR', 

# Invalid Strings (Should not match)
    'CALEB',     
    'CERTAB',    
    'CAL',   
]

# Test the regular expression against each string

for test_string in test_strings:
    if regex.match(pattern, test_string):
        print(f"'{test_string}' matches the pattern.")
    else:
        print(f"'{test_string}' does not match the pattern.")
