# Databricks notebook source
# MAGIC %md
# MAGIC Gets transaction features for specific time window

# COMMAND ----------

from pyspark.sql.functions import col, explode, expr, to_date, size, count, when, lit
from pyspark.sql.functions import sum as _sum, round as _round
from pyspark.sql import DataFrame
from functools import reduce

# COMMAND ----------

from data_utils.spark_utils import create_feature_table, get_environment_paths, get_spark
from data_utils.data_persistence import persist_table

# COMMAND ----------

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

spark = get_spark()

# COMMAND ----------
# Set up widget and get parameter
# dbutils.widgets.text("window", "")
filter_x_days_str = dbutils.widgets.get("window")

if not filter_x_days_str:
    raise ValueError("The parameter 'time-window' must be set in the notebook parameters.")

try:
    filter_x_days = int(filter_x_days_str)
except ValueError:
    raise ValueError("The parameter 'time-window' must be an integer representing the number of days.")

if filter_x_days <= 0:
    raise ValueError("The parameter 'time-window' must be a positive integer representing the number of days.")

logger.info(f"Filtering data for the last {filter_x_days} days.")
