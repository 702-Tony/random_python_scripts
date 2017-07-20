import os

#Runs on Windows only

print 'Welcome! this program will find files with pathnames that are too long'.center(80, '+')

filename = raw_input('Name output file: ')

if filename[-4:] != '.txt': filename += '.txt'

outputfile = open(filename,'w')# opens file matching name, otherwise creates file if not found


dir = str(raw_input('Which directory? '))
if dir[0] == 'J':
    serverpath = 11
elif dir[0] == 'K':
    serverpath = 8
else :
    serverpath = 0

os.chdir(dir)

count = 0

print 'working...'

for root, dirs, files in os.walk('.'):
    
    for i in files:
        
        x = (root +'\\' + i )[2:] #removes ./ from filename and assigns full filepath to directory
        
        if (len(x)+serverpath) > 255:
            #print 'Files written: ' + str(count +1)
            #print (dir + '\\' + x + '\n')
            #print len(x)
            outputfile.write(dir + '\\' + x + '\n')
            count +=1
    
    

print 'Done: total lines written: ' + str(count)

outputfile.close()

