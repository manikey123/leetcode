import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, upper, avg
os.environ["HADOOP_HOME"] = r"C:\hadoop-3.3.0"
os.environ["PATH"] += os.pathsep + os.environ["HADOOP_HOME"] + "\\bin"

# Setting the environment variables for PySpark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Initialize a SparkSession
spark = SparkSession.builder.appName("partitionBy example").getOrCreate()

# Create an RDD
data = [("cat", 1), ("dog", 2), ("cat", 3), ("dog", 1), ("cat", 5)]
rdd = spark.sparkContext.parallelize(data)

# Using groupByKey()
grouped = rdd.groupByKey().mapValues(list)
print("groupByKey results:")
print(grouped.collect())

# Using reduceByKey()
reduced = rdd.reduceByKey(lambda a, b: a + b)
print("reduceByKey results:")
print(reduced.collect())

# Using aggregateByKey()
# Zero value: the initial value for the accumulator for each key
zero_value = 0

# SeqOp: the operation to apply to the accumulator and each value in the RDD for the same key
seqOp = lambda acc, value: acc + value

# CombOp: the operation to apply to merge accumulators for the same key
combOp = lambda acc1, acc2: acc1 + acc2

aggregated = rdd.aggregateByKey(zero_value, seqOp, combOp)
print("aggregateByKey results:")
print(aggregated.collect())

# Stop the Spark session
spark.stop()



# groupByKey results:
# [('dog', [2, 1]), ('cat', [1, 3, 5])]
# reduceByKey results:
# [('dog', 3), ('cat', 9)]
# aggregateByKey results:
# [('dog', 3), ('cat', 9)]