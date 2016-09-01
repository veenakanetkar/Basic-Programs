import os

path = ('D:\codep\my_folder')
if not os.path.exists(path):
	os.path.mkdirs(path)