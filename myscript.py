import os
import fnmatch
import re
for root, dir, files in os.walk("."):
        for items in fnmatch.filter(files, "*.txt"):
                path = root + '/' + items
                data = open(path, 'r')
                numbers = data.read()

                r = re.compile(r'(?<!\d)[789]\d{4}[-\.\s]??\d{5}|(?<!\d)[789]\d{2}[-\.\s]??\d{3}[-\.\s]??\d{4}')

                results = r.findall(numbers)
                if results:
                	#results = map(str.strip, results)
                	print results