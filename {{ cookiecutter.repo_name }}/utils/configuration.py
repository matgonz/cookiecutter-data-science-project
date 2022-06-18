# Databricks notebook source
# MAGIC %md
# MAGIC # Imports
# MAGIC 
# MAGIC Next steps:
# MAGIC - Include openpyxl in requirements.txt
# MAGIC - Set requirements.txt on cluster prebuild

# COMMAND ----------

!pip3 install openpyxl

# COMMAND ----------

import pyspark
import numpy as np

# COMMAND ----------

# MAGIC 
# MAGIC %md
# MAGIC ### Define Data Paths

# COMMAND ----------

#projectPath     = f"/dbacademy/{username}/mlmodels/profile/"
projectPath = ""

goldPath = projectPath + "gold/"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Configure Feature Store Database

# COMMAND ----------

feature_store_database_name = "fs_ecommerce"

spark.sql(f"CREATE DATABASE IF NOT EXISTS {feature_store_database_name}")
