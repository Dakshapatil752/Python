"""
Examples: Using different Python packages
"""

# os: Operating system interfaces
import os
print("List of files in current directory:", os.listdir('.'))

# sys: System-specific parameters and functions
import sys
print("Command line arguments:", sys.argv)

# math: Mathematical functions
import math
print("Cosine of 0:", math.cos(0))

# datetime: Date and time manipulation
import datetime
print("Today's date:", datetime.date.today())

# json: JSON parsing and encoding
import json
data = {'x': 1, 'y': 2}
json_str = json.dumps(data)
print("JSON string:", json_str)

# re: Regular expressions
import re
match = re.search(r'\d+', 'abc123def')
print("First number in string:", match.group() if match else None)

# collections: Container datatypes
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print("Deque after append:", queue)

# random: Random number generation
import random
print("Random float between 0 and 1:", random.random())

# If you want examples for external packages like numpy, pandas, matplotlib, requests, let me know!
