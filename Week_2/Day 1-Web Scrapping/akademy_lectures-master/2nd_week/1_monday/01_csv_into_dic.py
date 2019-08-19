import csv

with open('./data/beers.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\tThe beer {row["Name"]} is {row["Appearance"]}, and it is from {row["Origin"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
