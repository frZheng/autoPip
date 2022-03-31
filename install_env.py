import os
import sys
print(len(sys.argv))
#exit()
if len(sys.argv) == 2:
    file_name = sys.argv[1]
    with open(file_name,"r",encoding="utf-8") as fin:
        lines = fin.readlines()
        for line in lines:
            if line[-1] == "\n":
                line = line[:-1]
            cmd = "pip install --no-dependencies  " + line
            print(cmd)
            os.system(cmd)
else:
    print("file len error")