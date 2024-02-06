import os
import sys

# Set the PySpark Python environment variables
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
from pyspark import SparkContext

# Initialize a SparkContext
sc = SparkContext("local", "Simple RDD Example")
print("sc",sc)

# Create an RDD from a list of numbers
numbers = [1, 2, 3, 4, 5]
numbers_rdd = sc.parallelize(numbers)
print(numbers_rdd)
# Square the numbers
squared_rdd = numbers_rdd.map(lambda x: x ** 2)

# Filter out even numbers
filtered_rdd = squared_rdd.filter(lambda x: x % 2 == 0)

# Collect the results back to the driver program
results = filtered_rdd.collect()

# Print the results
print("Squared and filtered numbers:", results)

# Stop the SparkContext
sc.stop()