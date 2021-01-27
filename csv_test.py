# csv_test
# i plan on trying to open a csv and iterate through the row like a list

import csv
# instantiate helper vars
n_line_yr = -1
s_line_yr = -1
output_n = []
output_s = []
# builds a clean list with 14 empty spots
def build_list():
    new_list = []
    for i in range(14):
        new_list.append('')
    return new_list
# open old csv
with open('seaice_avg.csv', newline='') as csvfile:
    csv_r = csv.reader(csvfile, delimiter=' ', quotechar='|')
    line_n = build_list()
    line_s = build_list()
    count = 0
    # iterate through the rows and store the data for each month in a list
    # that will then be stored inside another list
    for row in csv_r:
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
            line_n[13] = hemisphere
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
            line_s[13] = hemisphere
# append final lines to outputs
output_n.append(line_n)
output_s.append(line_s)
# output file
print('csv successfully read')
with open('sea_ice_averages_transformed.csv', 'w', newline='') as csvfile:
    csv_w = csv.writer(csvfile, delimiter=',',quotechar='\'', quoting=csv.QUOTE_MINIMAL)
    # removes first blank from both lists
    output_n.pop(0)
    output_s.pop(0)
    # # adds hemisphere data from
    # for i in output_n:
    #     i.append('north')
    # for i in output_s:
    #     i.append('south')
    header = ['year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec','hemisphere']
    csv_w.writerow(header)
    csv_w.writerows(output_n)
    csv_w.writerows(output_s)
print('csv successfully written')
