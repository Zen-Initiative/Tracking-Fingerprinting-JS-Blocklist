#!/usr/bin/python3

# Adapted from https://gitlab.com/malware-filter/tracking-filter/-/tree/main/src
# Converted to python with changes and tweaks

# Extract tracking JS URLs from DuckDuckGo Tracker Radar data 
# High-certainty URLs Only: fingerprinting = 3 (see https://github.com/duckduckgo/tracker-radar/blob/main/docs/FAQ.md)

import os
import json

outputFile = os.path.join(os.path.dirname(__file__), 'tracking-js-high-URLs.txt')

domains = os.path.join(os.path.dirname(__file__), '../domains')
countries = os.listdir(domains)

unique_links = set()  # Initialize an empty set to store unique links (a set only stores unique elements)

for country in countries:
    files = os.listdir(os.path.join(domains, country))
    for file in files:
        with open(os.path.join(domains, country, file), 'r', encoding="utf-8") as f:
            data = json.load(f)
            resources = data['resources']
            tracking = [resource for resource in resources if resource['fingerprinting'] == 3]
            for track in tracking:
                link = track['rule'].replace('\\', '').replace('^www.', '')
                if link.endswith('.js'):
                    unique_links.add(link)  # Add the link to the set of unique links 

with open(outputFile, 'w') as out: # Write the unique links to the output file (overwriting existing file)
    sorted_links = sorted(unique_links)  # Sort the unique links alphabetically
    for link in sorted_links:
        out.write(link + '\n')


# Extract tracking JS URLs from DuckDuckGo Tracker Radar data 
# Possible tracking URLs Only: fingerprinting = 2 (see https://github.com/duckduckgo/tracker-radar/blob/main/docs/FAQ.md)

outputFile = os.path.join(os.path.dirname(__file__), 'tracking-js-possible-URLs.txt')

domains = os.path.join(os.path.dirname(__file__), '../domains')
countries = os.listdir(domains)

unique_links = set()  # Initialize an empty set to store unique links (a set only stores unique elements)

for country in countries:
    files = os.listdir(os.path.join(domains, country))
    for file in files:
        with open(os.path.join(domains, country, file), 'r', encoding="utf-8") as f:
            data = json.load(f)
            resources = data['resources']
            tracking = [resource for resource in resources if resource['fingerprinting'] == 2]
            for track in tracking:
                link = track['rule'].replace('\\', '').replace('^www.', '')
                if link.endswith('.js'):
                    unique_links.add(link)  # Add the link to the set of unique links 

with open(outputFile, 'w') as out: # Write the unique links to the output file (overwriting existing file)
    with open('tracking-js-high-URLs.txt', 'r', encoding="utf-8") as f1:
        existing_links = f1.read().splitlines() 
    final_links = set(set(unique_links) - set(existing_links))
    sorted_links = sorted(final_links)  # Sort the final links alphabetically
    for link in sorted_links:
        out.write(link + '\n')


# Convert the lists to uBO syntax filter lists:

from datetime import datetime, timezone

CURRENT_TIME = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

TITLE1 = "! Title: 🔒 Tracking (Fingerprinting) JS Blocklist - High Certainty"
TITLE2 = "! Title: 🔏 Tracking (Fingerprinting) JS Blocklist - Possible tracking JS"
TITLE3 = "! Title: 🔒🔒 Tracking (Fingerprinting) JS Blocklist - High Certainty - strict"
TITLE4 = "! Title: 🔏🔏 Tracking (Fingerprinting) JS Blocklist - Possible tracking JS - strict"
SOURCE = "! Source: DuckDuckGo Tracker Radar (https://github.com/duckduckgo/tracker-radar)"
TIME = f"! Updated: {CURRENT_TIME}"
EXPIRE = "! Expires: 31 days (update frequency depends on upstream source)"
HOME = "! Homepage: https://github.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist"
LICENSE = "! License: https://github.com/Zen-Initiative/Tracking-Fingerprinting-JS-Blocklist/blob/main/README.md#license"
EMPTY_LINE = "!----------------------------------------------------------------------------------------------------------------!"

COMMENT_UBO1 = f"{TITLE1}\n{SOURCE}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n{EMPTY_LINE}"
COMMENT_UBO2 = f"{TITLE2}\n{SOURCE}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n{EMPTY_LINE}"
COMMENT_UBO3 = f"{TITLE3}\n{SOURCE}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n{EMPTY_LINE}"
COMMENT_UBO4 = f"{TITLE4}\n{SOURCE}\n{TIME}\n{EXPIRE}\n{HOME}\n{LICENSE}\n{EMPTY_LINE}"

# Convert the High Certainty list:

with open('tracking-js-high-URLs.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

    modified_lines = ['||' + line.strip() for line in lines]
    modified_lines_strict = ['||' + line.strip() + '$all,~doc,~popup' for line in lines]  

    modified_lines.insert(0, COMMENT_UBO1)
    modified_lines_strict.insert(0, COMMENT_UBO3)

with open('tracking-js-high-uBO.txt', 'w', encoding="utf-8") as file:
    file.write('\n'.join(modified_lines))
    
with open('tracking-js-high-uBO-strict.txt', 'w', encoding="utf-8") as file:
    file.write('\n'.join(modified_lines_strict))


# Convert the Possible Tracking JS list:
    
with open('tracking-js-possible-URLs.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

    modified_lines = ['||' + line.strip() for line in lines]
    modified_lines_strict = ['||' + line.strip() + '$all,~doc,~popup' for line in lines]  
    
    modified_lines.insert(0, COMMENT_UBO2)
    modified_lines_strict.insert(0, COMMENT_UBO4)

with open('tracking-js-possible-uBO.txt', 'w', encoding="utf-8") as file:
    file.write('\n'.join(modified_lines))

with open('tracking-js-possible-uBO-strict.txt', 'w', encoding="utf-8") as file:
    file.write('\n'.join(modified_lines_strict))