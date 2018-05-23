import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
thefile = open('File_names.txt', 'w')
for f in files:
	thefile.write("%s\n" % f)
for f in files:
	print(f)
print("All file listed in File_names.txt.")
