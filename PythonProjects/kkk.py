import sys
import os
if sys.platform == 'darwin':
    print ('Hello Mac!')
elif sys.platform == 'linux':
    print ('Hello Linux!')
elif sys.platform == 'win32':
    print ('Hello Windows!')

print (os.listdir())
