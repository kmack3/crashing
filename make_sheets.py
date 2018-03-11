import csv

arr = [150, 6000, 10000, 55000, 110000]
for num in arr:
    outname = "airbnb" + str(num) + ".csv"
    with open('airbnb.csv', 'r') as infile:
        with open(outname, 'w') as outfile:
            reader = csv.reader(infile, delimiter=',')
            writer = csv.writer(outfile, delimiter=',')
            count = 0
            for row in reader:
                if (count < num):
                    writer.writerow(row)
                    count+=1
