import re

# Specify the file path
file_path = "links.txt"  # Replace with your file's path

try:
    # Open the file in read mode ('r')
    with open(file_path, 'r') as file:
        # Read the entire file content into a string
        input_text = file.read()

    # Define a regular expression pattern to match links within HTML attributes
    link_pattern = r'href="([^"]+)"'

    # Find all matches of the pattern in the input text
    matches = re.findall(link_pattern, input_text)

    # Print the detected links
    for match in matches:
        print(match)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
