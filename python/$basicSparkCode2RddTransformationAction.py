import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
from pyspark import SparkContext

# Initialize SparkContext
sc = SparkContext("local", "RDD Operations Example")

# Sample data
data1 = [1, 2, 3, 4, 5]
data2 = [4, 5, 6, 7, 8]

# Creating RDDs
rdd1 = sc.parallelize(data1)
rdd2 = sc.parallelize(data2)

# Transformation: map
mapped_rdd = rdd1.map(lambda x: x * 2)

# Transformation: filter
filtered_rdd = rdd1.filter(lambda x: x % 2 == 0)

# Transformation: flatMap
flat_mapped_rdd = rdd1.flatMap(lambda x: (x, x * 2))

# Transformation: union
union_rdd = rdd1.union(rdd2)

# Transformation: distinct
distinct_rdd = union_rdd.distinct()

# Action: collect
collected_data = distinct_rdd.collect()

# Action: count
count_data = distinct_rdd.count()

# Action: take
take_data = distinct_rdd.take(3)

# Action: reduce
sum_data = rdd1.reduce(lambda x, y: x + y)

# Print results
print("Collected Data:", collected_data)
print("Count of Distinct Elements:", count_data)
print("First 3 Elements:", take_data)
print("Sum of Elements in RDD1:", sum_data)

# Stop the SparkContext
sc.stop()
