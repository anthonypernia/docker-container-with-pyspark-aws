# This script is used to test error handling within the program.
# It creates a DataFrame with 3 columns and 3 rows, then deliberately raises an error.

from pyspark.sql import SparkSession
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize a Spark session with a custom application name and configuration
spark = SparkSession.builder \
    .appName("Test Logs in Spark") \
    .config("spark.sql.shuffle.partitions", "2").getOrCreate()  #Reduce shuffle partitions for simplicity
    
# Create a sample DataFrame
logger.info("Creating a sample DataFrame...")
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, schema=columns)

# Display the DataFrame
logger.info("Displaying the contents of the DataFrame...")
df.show()

# Apply a transformation: filter rows where age is greater than 30
logger.info("Filtering the DataFrame for ages greater than 30...")
filtered_df = df.filter(df.Age > 30)

# Display the filtered results
logger.info("Displaying results after filtering:")
filtered_df.show()

# Attempt to select a column ("City") that does not exist
# This will raise an error to test error handling
logger.info("Attempting to select a non-existent column 'City' (this will raise an error)...")
selected_df = filtered_df.select("Name", "Age", "City")  # This will raise an error
selected_df.show()
