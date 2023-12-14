import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Basic PySpark Example") \
    .getOrCreate()

# Sample data
data = [("James", "Smith", 30),
        ("Anna", "Rose", 41),
        ("Robert", "Williams", 62)]

# Specify column names
columns = ["FirstName", "LastName", "Age"]

# Create a DataFrame from the data
df = spark.createDataFrame(data, columns)

# Perform a simple transformation: filter and select
filtered_df = df.filter(col("Age") > 40).select("FirstName", "LastName")

# Show the results
filtered_df.show()

# Stop the SparkSession
spark.stop()