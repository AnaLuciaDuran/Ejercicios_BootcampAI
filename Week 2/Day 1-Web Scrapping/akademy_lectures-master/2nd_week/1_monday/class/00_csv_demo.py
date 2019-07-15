import csv

with open('./data/beers.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t The beer {row[0]} is {row[1]}, and it is from {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
