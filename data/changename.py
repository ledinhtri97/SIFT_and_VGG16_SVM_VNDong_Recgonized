import os
 
path = input("Enter the directory path where you need to  rename: ")
i = 1
for filename in os.listdir(path):
	filename_without_ext = os.path.splitext(filename)[0]
	# extension = os.path.splitext(filename)[1]
	extension = '.jpg'
	new_file_name = str(i)
	i+=1
	new_file_name_with_ext = new_file_name+extension
	print(new_file_name_with_ext)
	os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext))