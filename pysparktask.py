from pyspark.sql import SparkSession
import pyspark
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('task2').getOrCreate()
categories = spark.createDataFrame([
    (1, "category1"),
    (2, "category2"),
    (3, "category3"),
    (4, "category4"),
    (5, "category5"),
    (6, "category6"),
    (7, "category7"),
    (8, "category8"),
    (9, "category9"),
],
    ["id", "category_name"],
)
products = spark.createDataFrame([
    (1, "product1"),
    (2, "product2"),
    (3, "product3"),
    (4, "product4"),
    (5, "product5"),
    (6, "product6"),
    (7, "product7"),
    (8, "product8"),
    (9, "product9"),
],
    ["id", "product_name", ]
)
ER_table_products_vs_categories = spark.createDataFrame([
    (1, 1),
    (2, 8),
    (3, 7),
    (4, 5),
    (6, 3),
    (7, 4),
    (9, 6),
    (8, 1),

],
    ["product_id", "category_id", ]
)
result = (products.join(ER_table_products_vs_categories,
                        products.id == ER_table_products_vs_categories.product_id, how='left')
          .join(categories,
                ER_table_products_vs_categories.category_id == categories.id, how='left')
          .select(['product_name', 'category_name'])
          )

result.orderBy("product_id", "category_id", ).show(truncate=True)
