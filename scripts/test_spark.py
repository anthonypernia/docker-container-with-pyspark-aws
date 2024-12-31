from pyspark.sql import SparkSession
import logging

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Start a Spark session
    logger.info("Starting the Spark session...")
    spark = SparkSession.builder \
        .appName("Test Logs in Spark") \
        .config("spark.sql.shuffle.partitions", "2").getOrCreate()   # Set shuffle partitions for optimization
        

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

    # Count the number of records in the filtered DataFrame
    count = filtered_df.count()
    logger.info(f"The filtered DataFrame contains {count} records.")

    # Stop the Spark session
    logger.info("Stopping the Spark session...")
    spark.stop()

if __name__ == "__main__":
    main()
