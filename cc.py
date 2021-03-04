import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random
df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()
mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
stddeviation1 = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
stddeviation2 = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
stddeviation3 = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is ",mean)
print("Median of this data is ",median)
print("Mode of this data is ",mode)
print("Standard deviation of this data is {}".format(std_deviation))
print(len(stddeviation1)*100/len(data),"% of data lies within 1 standard deviation")
print(len(stddeviation2)*100/len(data),"% of data lies within 2 standard deviations")
print(len(stddeviation3)*100/len(data),"% of data lies within 3 standard deviations")