import os
import sys
#tested on Windows only

print 'Welcome! this program will find files with pathnames that are too long'.center(80, '+')
if len(sys.argv) > 1:
    if sys.argv[1] == '--csv':
        filename = raw_input('Name output file(file output in .csv format): ')
        if filename[-4:] != '.csv': filename += '.csv'
        csv = True
    elif sys.argv[1] == '--txt' :
        filename = raw_input('Name output file(file output in .txt format): ')
        if filename[-4:] != '.txt': filename += '.txt'
        csv = False
    else :
        filename = raw_input('Name output file(file output in .txt format): ')
        if filename[-4:] != '.txt': filename += '.txt'
        csv = False


outputfile = open(filename,'w')# opens file matching name, otherwise creates file if not found


dir = str(raw_input('Which directory? '))
#below, serverpath adds length to file path to represent server path since running remotely
if dir[0] == 'J':
    serverpath = 11
elif dir[0] == 'K':
    serverpath = 8
else :
    serverpath = 0

os.chdir(dir)

count = 0

print 'working...'

if csv == True: outputfile.write('File Path Length,Filepath 1, Filepath 2\n')

for root, dirs, files in os.walk('.'):
    
    for i in files:
        if serverpath == 0: serverpath = len(dir)#changes serverpath to length reflected on current drive if not server drive J or K
        x = (root +'\\' + i )[2:] #removes ./ from filename and assigns full filepath to directory
        
        if (len(x)+serverpath) > 255:
            #print 'Files written: ' + str(count +1)
            #print (dir + '\\' + x + '\n')
            #print len(x)
            if csv == True:
                outputfile.write(str(len(x)+serverpath)+','+ dir + ',' + x + '\n')
            else: outputfile.write(dir + '//' + x + '\n')
            
            count +=1
    
    

print 'Done: total files found: ' + str(count)

outputfile.close()

