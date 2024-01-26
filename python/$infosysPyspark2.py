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

# Sample data
data = [("James", "Sales", 3000),
        ("Michael", "Sales", 4600),
        ("Robert", "HR", 4100),
        ("Maria", "Finance", 3000),
        ("James", "Finance", 3000),
        ("Scott", "Finance", 3300),
        ("Jen", "Finance", 3900),
        ("Jeff", "Marketing", 3000),
        ("Kumar", "Marketing", 2000),
        ("Saif", "Sales", 4100)]

# Define schema
columns = ["EmployeeName", "Department", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, schema=columns)
# Specify the path where you want to save the partitioned data
# output_path = "/path/to/output/directory"

# Write and partition the DataFrame by 'Department'
df.write.mode("overwrite").partitionBy("Department").csv('cow')   #append
# df.write.csv()   #append
