# csv_test
# i plan on trying to open a csv and iterate through the row like a list

import csv
# months = ["","1","2","3","4","5","6","7","8","9","10","11","12"]

# open csv files
# csv = opencsv # for data that will be moved
# col_csv = opencsv # for where the data will be moved to
# iterate through each row

n_line_yr = -1
s_line_yr = -1
output_n = []
output_s = []
def build_list():
    new_list = []
    for i in range(13):
        new_list.append('')
    return new_list

with open('seaice_avg.csv', newline='') as csvfile:
    csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
    line_n = build_list()
    line_s = build_list()
    count = 0
    for row in csv:
        count += 1
        rw_ls = row[0].split(',')
        year = rw_ls[0]
        if count > 1:
            mon = int(rw_ls[1])

        hemisphere = rw_ls[2]
        extent_avg = rw_ls[3]
        if hemisphere == 'north':
            # new_year = new_line
            if n_line_yr != year:
                # append finished line to output
                output_n.append(line_n)
                # clear line
                line_n = build_list()
                # set new line_yr to current
                n_line_yr = year
            # put your data together
            line_n[0] = n_line_yr
            line_n[mon] = extent_avg
        elif hemisphere == 'south':
            if s_line_yr != year:
                # append finished line to output
                output_s.append(line_s)
                # clear line
                line_s = build_list()
                # set new line_yr to current
                s_line_yr = year
            line_s[0] = s_line_yr
            line_s[mon] = extent_avg


print('items done',output_n[1],output_s[1])
        # rw_ls = list(row)
        # year = rw_ls[0]
        # mon = int(rw_ls[1])
        # hemisphere = rw_ls[2]
        # extent_avg = rw_ls[3]
        # if line_yr != year:
        #     # append finished line to output
        #     output.append(line)
        #     # clear line
        #     line = []
        #     # set new line_yr to current
        #     line_yr = year
