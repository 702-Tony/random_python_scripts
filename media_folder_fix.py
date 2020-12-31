import os
# this script will be used to 
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
