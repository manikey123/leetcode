import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, upper, avg
os.environ["HADOOP_HOME"] = "C:\\hadoop"
os.environ["PATH"] += os.pathsep + os.environ["HADOOP_HOME"] + "\\bin"

# Setting the environment variables for PySpark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Initialize a SparkSession
spark = SparkSession.builder.appName("read CSV example").getOrCreate()


# Path to your CSV file (could be a local path or HDFS, S3, etc.)
csv_file_path = "inputData\EmpDept.csv"

# Read the CSV file into a DataFrame
df = spark.read.csv(csv_file_path, header=True, inferSchema=True)

# Output path for the new CSV file
output_csv_file_path = "EmpDept_new.csv"

# Write the DataFrame into a CSV file and overwrite if the file already exists
df.write.csv(path=output_csv_file_path, mode="overwrite", header=True)



# Show the DataFrame
df.show()