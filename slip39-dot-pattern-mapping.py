#!/usr/bin/python3
import urllib.request
from collections import defaultdict

# Fetch official SLIP39 wordlist
url = 'https://raw.githubusercontent.com/satoshilabs/slips/master/slip-0039/wordlist.txt'
with urllib.request.urlopen(url) as response:
    wordlist = [word.strip() for word in response.read().decode().splitlines()]

# Generate the data: for each word, we have index and the two column patterns
data = []
for i, word in enumerate(wordlist):
    index = i + 1
    # Convert index to 12-bit binary string (1-1024, padded with leading zeros)
    bin_str = bin(index)[2:].zfill(12)
    # Split into three 4-bit groups
    col1_bin = bin_str[0:4]
    col2_bin = bin_str[4:8]
    col3_bin = bin_str[8:12]
    
    # Store both binary and dot patterns
    col1_dot = ''.join('●' if bit == '1' else '○' for bit in col1_bin)
    col2_dot = ''.join('●' if bit == '1' else '○' for bit in col2_bin)
    col3_dot = ''.join('●' if bit == '1' else '○' for bit in col3_bin)
    
    data.append((index, word, col1_bin, col2_bin, col3_bin, col1_dot, col2_dot, col3_dot))

# Generate markdown table in the correct format
header = "| Index   | Word       | 2048 1024 512 256 | 128 64 32 16 | 8 4 2 1 |\n"
header += "|---------|------------|-------------------|--------------|---------|\n"

rows = []
for entry in data:
    index, word, _, _, _, col1, col2, col3 = entry
    rows.append(f"| {index:7} | {word:10} | {col1:^17} | {col2:^12} | {col3:^7} |")

md_content = '# SLIP39 Dot Pattern Mapping\n\n' + header + '\n'.join(rows)

# Save to file
with open('slip39-dot-pattern-mapping.md', 'w') as f:
    f.write(md_content)