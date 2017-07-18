import os



print 'Welcome! this program will find files with pathnames that are too long'.center(80, '+')
fname = raw_input('Name output file: ')
if fname[-4:-1] != '.txt': fname += '.txt'
outputfile = open(fname,'w')# opens file matching name, otherwise creates file if not found

dir = str(raw_input('Which directory? '))
os.chdir(dir)

count = 0

print 'working...'

for root, dirs, files in os.walk('.'):
    
    for i in files:
        
        x = (root +'\\' + i )[2:] #removes ./ from filename and assigns full filepath to directory
        
        if (len(x)+len(dir)) > 255:
            #print 'Files written: ' + str(count +1)
            
            print len(x)
            outputfile.write(dir + '\\' + x + '\n')
            count +=1
    
    

print 'Done: total lines written: ' + str(count)

outputfile.close()


