import hashlib

def hash_lines(filename, hasher):
  """Hashes each line in a text file using the specified hashing algorithm.

  Args:
      filename: The path to the text file.
      hasher: The hashing function from the hashlib module (e.g. sha1, sha256).
  """
  with open(filename, 'r') as file:
    for line in file:
      # Remove trailing whitespace (like newline character)
      clean_line = line.strip()
      # Hash the cleaned line
      hash_value = hasher(clean_line.encode()).hexdigest()
      # Print the original line and its hash
      print(f"{clean_line}: {hash_value}")

# Example usage
filename = "list.txt"
hasher = hashlib.sha1

hash_lines(filename, hasher)




""""
output = hashlib.sha1(b'Machomet6')
print(output)
print(output.hexdigest())
"""
