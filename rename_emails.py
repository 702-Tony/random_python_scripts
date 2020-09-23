import extract_msg # this will need to be installed using pip. More info here: https://pypi.org/project/extract-msg/
import os
from datetime import datetime

# Folder that contains the emails to be renamed
filepath = "C:/Users/aadams/desktop/New Folder (7)/Exprt001"

# count to keep the emails
count = 0

for file in os.listdir(filepath):
	new_filepath = filepath + "/" + file
	# open message
	msg = extract_msg.openMsg(filepath + "/" + file)
	# store message
	_subject = msg.subject
	# create datetime obj from string extracted from message
	# pulled from message as : Wed, 29 Aug 2018 11:06:22 -0700
	_date = datetime.strptime(msg.date, '%a, %d %b %Y %H:%M:%S %z')
	# close message to allow rename
	msg.close()
	# increment counter to ensure messages are unique
	count += 1
	# create new name string with sent date, shortened subject, then count with padded zeroes
	new_name = _date.strftime('%Y-%m-%d %H%M%S') + "-" + _subject[:30] + str(count).zfill(4)
	# some subjects had ":"'s which cannot be saved to windows filenames
	# replace those with underscore
	new_name = new_name.replace(":","_")
	# perform rename. Something to add in future iterations would be a try except clause, but was not necessary for my purposes
	os.rename(new_filepath, filepath + "/" + new_name + ".msg")
