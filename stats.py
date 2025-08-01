import statistics

numbers = input("Enter numbers seperated by commas: ")
data = [float(num) for num in numbers.split(",")]

mean = statistics.mean(data)
median = statistics.median(data)

try:
    mode = statistics.mode(data)
except statistics.StatisticsError:
    mode = "No unique mode found"

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)