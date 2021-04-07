import re

my_string = "Let's write RegEx!"
pattern = r"\w+"
print(re.findall(pattern, my_string))