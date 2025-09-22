import re
text="the quick brown function jumps the overlay dog"

pattern=r"brown"
replacement="red"

new_text = re.sub(pattern, replacement, text)

print("the replacement text is:",new_text)

o/p->the replacement text is: the quick red function jumps the overlay dog
