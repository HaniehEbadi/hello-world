import csv
from os import name, write
# For the average
from statistics import mean 
# For the problem of arranging data entry in dictionary
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        output = OrderedDict()
        for row in reader:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(int(score))
            output[name] = float(mean(scores))
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(output.items())
        output_file.close()


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        output = OrderedDict()
        for row in reader:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(float(score))
            output[name] = float(mean(scores))
        output = OrderedDict(sorted(output.items()))
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(output.items())
        output_file.close()


def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        output = OrderedDict()
        for row in reader:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(float(score))
            output[name] = float(mean(scores))
        output = OrderedDict(sorted(output.items(), key= lambda t:(-t[1],t[0])))
        while len(output) > 3:
            output.popitem()
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(output.items())
        output_file.close()


def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        output = OrderedDict()
        for row in reader:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(float(score))
            output[name] = float(mean(scores))
        averagelistfloat = list(output.values())
        averagelistfloat.sort()
        averagelist = dict()
        i = 0
        for item in averagelistfloat:
            averagelist[i] = [str(item)]
            i += 1
        while len(averagelist) > 3:
            averagelist.popitem()
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(averagelist.values())
        output_file.close()


def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        output = OrderedDict()
        for row in reader:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(float(score))
            output[name] = float(mean(scores))
        averages = list(output.values())
        average = list()
        average.append(mean(averages))
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(average)
        output_file.close()