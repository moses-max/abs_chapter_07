import re

vRegex = re.compile(r'[aeiou]', re.I)
title = 'Human Physiology and Mechanisms of Diease'
print('Vowels:')
print(vRegex.findall(title))


NVRegex = re.compile(r'[^aeiou]', re.I)
print('Nonvowels:')
print(NVRegex.findall(title))