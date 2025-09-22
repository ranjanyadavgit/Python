import re

text="apple,banana,mango,papaya"
pattern=r","

new_text=re.split(pattern,text)

print("the split text is:",new_text)

