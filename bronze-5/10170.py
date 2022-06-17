west_teams = ['NFC West', '---------------', 'Seattle', 'San Francisco', 'Arizona', 'St. Louis']
west_w = ['W', '----', '13', '12', '10', '7']
west_l = ['L', '---', '3', '4', '6', '9']
west_t = ['T', '-', '0', '0', '0', '0']

north_teams = ['NFC North', '---------------', 'Green Bay', 'Chicago', 'Detroit', 'Minnesota']
north_w = ['W', '---', '8', '8', '7', '5']
north_l = ['L', '--', '7', '8', '9', '10']
north_t = ['T', '---', '1', '0', '0', '1']

for i in range(len(west_teams)):
    print(west_teams[i].ljust(15) + west_w[i].ljust(4) + west_l[i].ljust(3) + west_t[i].ljust(1))

print()

for i in range(len(north_teams)):
    print(north_teams[i].ljust(15) + north_w[i].ljust(3) + north_l[i].rjust(2) + north_t[i].rjust(3))