import os

LOCATION="respublic kazakhstan"
CATEGORY ="work"
path ="./"+LOCATION+"/"+CATEGORY

access_rights = 0o755

try:
    os.mkdir(path, access_rights)
except OSError:
    print("Error occured")
else:
    print("success")