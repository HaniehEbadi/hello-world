import csv
# For the average
from statistics import mean 
# For the problem of arranging data entry in the dictionary
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as input_file:
        input_file = csv.reader(input_file)
        output_file = open(output_file_name, 'w')
        writer = csv.writer(output_file)
        output = list()
        for row in input_file:
            name = row[0]
            scores = list()
            for score in row[1:]:
                scores.append(int(score))
            average = float(mean(scores))
            information = [name,str(average)]
            output.append(information)
        for i in range(0,len(output)):
            writer.writerow(output[i])
        output_file.close()



#def calculate_sorted_averages(input_file_name, output_file_name):
    


#def calculate_three_best(input_file_name, output_file_name):
    


#def calculate_three_worst(input_file_name, output_file_name):
    


#def calculate_average_of_averages(input_file_name, output_file_name):
    

calculate_averages('/Users/Hanie/Desktop/HANIEH/python/Project/inputfile.csv', '/Users/Hanie/Desktop/HANIEH/python/Project/outputfile.csv')