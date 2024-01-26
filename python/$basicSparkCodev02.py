import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, upper, avg

# Setting the environment variables for PySpark
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Enhanced PySpark Example") \
    .getOrCreate()

# Sample data
data = [("James", "Smith", 30),
        ("Anna", "Rose", 41),
        ("Robert", "Williams", 62),
        ("Michael", "Brown", 20),
        ("Jennifer", "Davis", 35)]

# Specify column names
columns = ["FirstName", "LastName", "Age"]

# Create a DataFrame from the data
df = spark.createDataFrame(data, columns)

# Additional transformations
# 1. Add a new column
df_with_new_column = df.withColumn("SeniorCitizen", col("Age") >= 60)

# 2. Change case of a column
df_uppercase = df_with_new_column.withColumn("FirstNameUpper", upper(col("FirstName")))

# 3. GroupBy and Aggregate
average_age = df.groupBy().avg("Age").withColumnRenamed("avg(Age)", "AverageAge")
# Additional GroupBy and Aggregate for 'SeniorCitizen'
average_age_by_seniority = df_with_new_column.groupBy("SeniorCitizen").avg("Age").withColumnRenamed("avg(Age)", "AverageAgeBySeniority")
# 4. Sorting
sorted_df = df.sort(col("Age").desc())

# Show the results of transformations
print("DataFrame with a new column 'SeniorCitizen':")
df_with_new_column.show()

print("DataFrame with uppercase first names:")
df_uppercase.show()

print("Average age in the data:")
average_age.show()



# Show the results of the new transformation
print("Average age by SeniorCitizen status:")
average_age_by_seniority.show()


print("Sorted DataFrame by age in descending order:")
sorted_df.show()

# Perform a filter and select as in the original script
filtered_df = df.filter(col("Age") > 40).select("FirstName", "LastName")

print("Filtered DataFrame (Age > 40):")
filtered_df.show()


# Spark Actions
# Count total rows in the original DataFrame
total_count = df.count()
print(f"Total count of rows in the original DataFrame: {total_count}")

# Collect and print the first row
first_row = df.first()
print(f"First row of the original DataFrame: {first_row}")

# Collect and print all rows (use with caution for large datasets)
all_rows = df.collect()
print("All rows in the original DataFrame:")
print(all_rows)

# Stop the SparkSession
spark.stop()
