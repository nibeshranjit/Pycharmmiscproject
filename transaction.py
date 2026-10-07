from pyspark.sql import SparkSession
import pyspark.sql.types as T

def ecommerce_transaction(spark):
    transaction_data = [(1, 101, 5001, 'Laptop', 'Electronics', 1000.0, 1),
                        (2, 102, 5002, 'Headphones', 'Electronics', 50.0, 2),
                        (3, 101, 5003, 'Book', 'Books', 20.0, 3),
                        (4, 103, 5004, 'Laptop', 'Electronics', 1000.0, 1),
                        (5, 102, 5005, 'Chair', 'Furniture', 150.0, 1)]

    transaction_schema = T.StructType([
        T.StructField("Transaction_id", T.IntegerType(), True),
        T.StructField("Customer_id", T.IntegerType(), True),
        T.StructField("Product_id", T.IntegerType(), True),
        T.StructField("Product_name", T.StringType(), True),
        T.StructField("Category", T.StringType(), True),
        T.StructField("Price", T.DoubleType(), True),
        T.StructField("Quantity", T.IntegerType(), True)
    ])

    df=spark.createDataFrame(transaction_data, transaction_schema)
    df.printSchema()
    df.show()

