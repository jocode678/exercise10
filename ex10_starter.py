import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
    print(hdir)
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)
print(filenames)

# TODO: use os.path.getsize to find each file's size
# Call it filename because you are looking at the individual item (filename) in the list (of filenames)
for filename in filenames:
    print(os.path.getsize(filename))

# TODO: Add a test to only display files that are not zero length
# If you define the variable within the previous loop, it will not know where to look if you use the variable in this loop. Hence define within the loop
# Define variable size in case it takes a long time to run the program, only want to run once
for filename in filenames:
    size = os.path.getsize(filename)
    if size != 0:
        print(filename, size)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
for name in filenames:
    print(os.path.basename(name))

