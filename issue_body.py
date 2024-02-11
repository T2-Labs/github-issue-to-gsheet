import re


# Given string
input_string = """### What term do you want to request obsoleting?
  
  MONDO:1234567
  
  ### What is the label of the term you want to request obsoleting?
  
  test term
  
  ### Obsoleteion reason
  
  option 2
  
  ### Explain why this term should be obsoleted
  
  testing..."""

# Split the string into lines
lines = input_string.split('\n')

# Initialize variables to store the extracted values
term_to_obsolete = None
term_label = None
obsoleteion_reason = None


for index, line in enumerate(lines):
  if line.strip() == '### What term do you want to request obsoleting?':
    term_to_obsolete = lines[index + 2].strip()  # Get the next non-empty line
  elif line.strip() == '### What is the label of the term you want to request obsoleting?':
    term_label = lines[index + 2].strip()
  elif line.strip() == '### Obsoleteion reason':
    obsoleteion_reason = lines[index + 2].strip()


# Output the extracted values
print("Term to obsolete:", term_to_obsolete)
print("Term label:", term_label)
print("Obsoletion reason':", obsoleteion_reason)
