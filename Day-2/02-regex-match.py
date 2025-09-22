import re

text="the quick brown fox"
pattern=r"the"

match=re.match(pattern, text)

if match:
   print("match found:",match.group())
else:
   pring("match didn't found")

o/p->match found: the



o/p->match found: the
