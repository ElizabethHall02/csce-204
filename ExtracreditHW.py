month_header = 'Su\tM\tTu\tW\tTh\tF\tSa'
months = { 'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 
    'June':30, 'July':31, 'August':31, 'September':30, 'October':31,
    'November':30, 'December':31 }

# loop through the dictionary of months
# k is the key (month name), v is the value (month length in days)
day_count = 0

 
for k,v in months.items():
    print(k) # print the month name
    print(month_header) # print the days header
    # loop through the numbers 1 through [month length]
    print('\t' * day_count, end='')
    for i in range(day_count % 7):
        # this will print the dates one per line, which is not correct
        print('\t', end='')
        # TODO: line up 7 in one line (tab-separated)
        
          
    for i in range(1, v + 1):
         print(i, end='\t')
         day_count += 1        
        # TODO: when you begin a new month, indent it the right number of spaces
         
         if day_count % 7 == 0:
             print()
              
    print('\n') #empty line between months
    