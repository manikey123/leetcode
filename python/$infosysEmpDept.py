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
# Path to your Parquet file
parquet_file_path = 'parquetInfosys.parquet'

# Read the Parquet file
df = spark.read.parquet(parquet_file_path)

# Show the DataFrame schema
df.printSchema()

# Show the contents of the DataFrame
df.show(truncate=False)

# Iterate through rows (if necessary)
# Note: It's more common to use DataFrame transformations in Spark rather than iterating
for row in df.collect():
    department = row['department']
    employees = row['employees']
    # Process each row as needed
    print(f"Department ID: {department['id']}, Department Name: {department['name']}")
    for employee in employees:
        print(f" - Employee: {employee['firstName']} {employee['lastName']}, Email: {employee['email']}, Salary: {employee['salary']}")

# Stop the SparkSession
spark.stop()

