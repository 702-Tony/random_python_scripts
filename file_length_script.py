import os



print 'Welcome! this program will find files with pathnames that are too long'.center(75, '+')
outputfile = open(raw_input('Name output file: '),'w')

os.chdir(str(raw_input('Which directory? ')))

count = 0

print 'working...'

for root, dirs, files in os.walk('.'):
    
    for i in files:
        
        x = (root +'\\' + i )[2:] #removes ./ from filename and assigns full filepath to directory
        
        if len(x) > 255:
            #print 'Files written: ' + str(count +1)
            print len(x)
            outputfile.write(x + '\n')
            count +=1
    
    

print 'Done: total lines written: ' + str(count)

outputfile.close()

