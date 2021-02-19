import csv
with open("skill2a.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
with open('skill2a.csv','r',newline="")as input,open('demo2.csv','w',newline="")as output:
    reader = csv.reader(input)
    writer = csv.writer(output)
    headerrow = next(reader)
    headerrow.append("totalsalary")
    writer.writerow(headerrow)
    for row in reader:
        totalsalary = round((float(row[3]) + float(row[4])),1)
        row.append(totalsalary)
        writer.writerow(row)
with open("demo2.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        if(float(row[5])<15000):
            print(row)