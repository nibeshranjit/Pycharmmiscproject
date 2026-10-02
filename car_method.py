from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from pyspark.sql.functions import col, lit
from pyspark.sql import SparkSession

def car_method(spark):
    car_schema = StructType([
        StructField("carr", StringType(), True),
        StructField("horsepower", IntegerType(), True),
        StructField("weight", IntegerType(), True),
        StructField("origin", StringType(), True)
    ])

    # 3. Raw Data
    car_data = [
        ("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
        ("BMW 2002", 113, 2234, "Europe")
    ]

    # 4. Create initial DataFrame
    df = spark.createDataFrame(data=car_data, schema=car_schema)

    # 5. Apply transformations
    transformed_df = df \
        .withColumnRenamed("carr", "car") \
        .withColumn("AvgWeight", lit(200)) \
        .withColumn("kilowatt_power", col("horsepower") * 1000)

    # 6. Show results and schema
    df.show(truncate=False)
    df.printSchema()
    transformed_df.show(truncate=False)
    transformed_df.printSchema()
    df.select("carr").show()