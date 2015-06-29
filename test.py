#!/usr/bin/python3.4
#
# REMEMBER NEWLINES MIGHT FUCK THIS UP, SO PUT END="" IN THE PRINT FUNCTION IF REQUIRED!
#

from bs4 import BeautifulSoup
import requests
import re
import subprocess, sys, os

url = "http://redd.it/341c03"
path = "/home/frederik/Documents/projects/DailyProgrammer/Challenge #212 [Easy] Rövarspråket/solution.py"
#print(path)

soup = BeautifulSoup(requests.get(url).text)

try:
	s = soup.select("div.md")[1].text
except Exception:
	print("Can't fetch reddit.")
	raise SystemExit

if len(s.split("Sample inputs & outputs")) > 1:
	s = s.split("Sample inputs & outputs")[1]
elif len(s.split("Sample Inputs and Outputs")) > 1:
	s = s.split("Sample Inputs and Outputs")[1]
elif len(s.split("Example inputs")) > 1:
	s = s.split("Example inputs")[1]

#print(s)
#print(s)

p = re.compile('Input\s*\d*\n(.*?)\n\nOutput\s*\d*\n(.*?)\n', re.DOTALL)

#for i, match in enumerate(re.findall(p, s)):
# 	print(match)

for i, match in enumerate(re.findall(p, s)):
	process = subprocess.Popen(
	    ["/usr/bin/python3.4", path],
	    shell  = False,
	    stdin  = subprocess.PIPE,
	    stdout = subprocess.PIPE,
	    stderr = subprocess.PIPE,
	    universal_newlines = True
	)
	#print("input", match[0])
	stdout, stderr = process.communicate(match[0])
	
	#print(repr(stdout))

	if stderr:
		print("Sample " + str(i + 1))
		print(stderr)
		continue

	#print(stdout, " == ", sample[2])
	if stdout == match[1] + "\n" or stdout == match[1]:
		print("Sample " + str(i + 1) + " √")
		#print(repr(stdout), " == ", repr(match[1]))
	else:
		print("Sample " + str(i + 1) + " X")
		print(repr(stdout), " == ", repr(match[1]))
