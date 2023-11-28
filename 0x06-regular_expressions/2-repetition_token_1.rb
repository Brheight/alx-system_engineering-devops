#!/usr/bin/env ruby

def match_regex(pattern, text):
    if re.search(pattern, text):
        print(text)
    else:
        print("")

patterns = [
    r"a(\w+)a",
    r"(\w+)a(\w+)",
    r"a(\w+)a(\w+)a",
]

texts = [
    "banana",
    "cataracts",
    "alligator",
]

for pattern in patterns:
    for text in texts:
        match_regex(pattern, text)
