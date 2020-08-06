# find_sender.py
import fileinput, re
pat = re.compile('From: (.*) <.*?>$',re.IGNORECASE)
pat2 = re.compile(r'[a-z\-\.]+@[a-z-\.]+',re.IGNORECASE)
for line in fileinput.input():
    m = pat.match(line)
    if m: print(m.group())






