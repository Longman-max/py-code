from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# Relative path

# if the Path is empty then it be relative to the current directory
path = Path('emails')
# Make a directory
print(path.mkdir())

# Remove a directory
print(path.rmdir())

# To check if a path exists in a directory
print(path.exists())

# iterating files in python

path = Path()

for file in path.glob('*'):
    print(file)

# we use the . to specify the file type e.g:
for file in path.glob('*.py'):
    print(file)
