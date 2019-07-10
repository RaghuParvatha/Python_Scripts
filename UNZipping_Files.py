# Below code extracts the data from a zip file into a folder called temp

from zipfile import ZipFile

filepath = '/Users/xyxz/abc/raw.zip'
extractfolderpath = '/Users/xyxz/abc/temp'
with ZipFile(filepath, 'r') as zipObj:
       # Extract all the contents of zip file in different directory
       zipObj.extractall(extractfolderpath)
