import sys
import os
cwd = os.getcwd()
sys.path.append(cwd)
#print(sys.path)

#Thest the module: generate_list
from generate_list() import printIt()
printIt()