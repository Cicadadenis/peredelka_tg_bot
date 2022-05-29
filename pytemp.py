import os 
import temp



t = temp.tempdir()

# Using PID in filename 
filename = '/tmp/journaldev.%s.txt' % os.getpid() # File mode is read write 
temp = open(filename, 'w+b') 
try: 
    print('temp: {0}'.format(temp)) 
    print('temp.name: {0}'.format(temp.name)) 
finally: temp.close() 
# Clean up the temporary file yourself 
os.remove(filename) 
print('TemporaryFile:') 
temp = tempfile.TemporaryFile() 
try: 
    print('temp: {0}'.format(temp)) 
    print('temp.name: {0}'.format(temp.name)) 
finally: # Automatically cleans up the 
    temp.close()
