# **Dockerized AWS Glue Environment**

## **Description**
This project provides a Dockerized environment to run data transformation scripts using PySpark with AWS Glue libraries in a local setup. It is ideal for testing and developing Glue jobs locally before deploying them to AWS.

The container includes configurations to interact with AWS using your local credentials, enabling you to emulate Glue jobs as if they were running on AWS Glue.

---

## **Features**
- Preconfigured environment with AWS Glue libraries (version 4.0).
- Direct interaction with AWS using your local credentials.
- Compatible with shared volumes for real-time work on your scripts.
- Support for Jupyter Notebook, PySpark, and Spark-submit.

---

## **Requirements**
- **Docker**
- **Docker Compose**
- AWS credentials configured in `~/.aws`.

---

## **Setup**
1. **Clone the repository**:
   ```bash
   git clone ""
   cd ""
   ```

2. **Configure the `.env` file**:
   Create a `.env` file in the root directory and define your AWS profile:
   ```plaintext
   PROFILE_NAME=default
   DISABLE_SSL=true
   ```
   - `PROFILE_NAME`: Specifies the AWS profile to be used (default: `default`).
   - `DISABLE_SSL`: Disables SSL for local testing (default: `true`).


You can add more variables to the `.env` file as needed.


3. **Project Structure**:
   Ensure that your scripts are placed in the `scripts/` folder. You can use the following structure:

   ```plaintext
   project/
   ├── docker-compose.yml
   ├── .env
   ├── scripts/
   │   ├── test_spark.py
   │   └── test_error.py
   ├── jupyter_workspace/
   │   └── test.ipynb
   ├── run_pyspark_remote_script.sh
   └── README.md
   ```


## **Usage**

### 1. Start the container
Run the container in detached mode using Docker Compose:

```bash
docker-compose up -d
```
### 2. Run a script in the container
Use the included Bash script to execute your scripts directly in the container. This script ensures the container is running and the file is located in the shared directory.


#### **Usage example:**
Create a script in `scripts/example_script.py` with the following content:

```python
from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("Example").getOrCreate()

# Sample data
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]

# Create a DataFrame
df = spark.createDataFrame(data, schema=columns)

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
```

```bash
./run_pyspark_remote_script.sh <file>.py
```
### 3. Access Jupyter Notebook
To explore and develop in an interactive environment, open Jupyter Notebook in your web browser using the following URL:

```plaintext
http://localhost:8888
```

### 4. Stop the container
Stop the container running in detached mode using Docker Compose:

```bash
docker-compose down
```
### 4. Inspect logs in real-time:
```bash
docker logs -f glue_jupyter_lab
```

## **FAQ / Troubleshooting**

- **Q: The container does not start properly. What can I do?**  
  A: Ensure Docker is installed and running, and that your AWS credentials are correctly configured in `~/.aws`.

- **Q: I cannot access Jupyter Notebook in the browser.**  
  A: Check that port 8888 is available and that the container is running properly.  
  If everything seems correct and Jupyter Notebook still doesn't work, follow these steps:

  1. Enter the container by running the following command:
     ```bash
     docker exec -it glue_jupyter_lab bash
     ```

  2. Inside the container, run the following commands:
     ```bash
     cd /home/glue_user/jupyter
     ./jupyter_start.sh
     ```

  This will start Jupyter Notebook inside the container, and you should be able to access it in your browser at `http://localhost:8888`.

