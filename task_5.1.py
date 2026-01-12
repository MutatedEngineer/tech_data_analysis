import csv
import statistics

with open('data-1768220513896.csv', 'r', encoding='utf-8') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=','))[1:]

reader = map(lambda x: (x[0], int(x[1])), reader)

sorted_reader = sorted(reader, key=lambda row: int(row[1]))
print(sorted_reader)
print()
print(sorted_reader[3])
print(sorted_reader[21])
print(sorted_reader[44])


print(round(sum(elem[1] for elem in sorted_reader) / len(sorted_reader), 2))
median_value = statistics.median(elem[1] for elem in sorted_reader)
print(median_value)
