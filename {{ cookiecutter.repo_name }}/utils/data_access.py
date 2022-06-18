# Databricks notebook source
# MAGIC %md
# MAGIC # Data Access Functions
# MAGIC 
# MAGIC **Create Feature Table**
# MAGIC 
# MAGIC In order to do this, we'll want to provide the following:
# MAGIC 1. The **name** of the database and table where we want to store the feature store
# MAGIC 2. The **keys** for the table
# MAGIC 3. The **schema** of the table
# MAGIC 4. A **description** of the contents of the feature store

# COMMAND ----------

def fs_create_table(df_features:pyspark.sql.DataFrame, database_name:str, feature_table_name:str, primary_keys:np.array, description:str):
    """
        Create Feature Table

        In order to do this, we'll want to provide the following:
            1. df_features: The data that will be load into Feature Table
            2. database_name: The name of database where we want to store the feature store
            3. feature_table_name: The name of table where we want to store the feature store
            4. primary_keys: The keys for the table
            5. description: A description of the contents of the feature store
            
        Use example:
            database_name = 'fs_ecommerce'
            feature_table_name = 'customers_features_test'
            primary_keys = ["CustomerID"]
            description = "This table contains one-hot and numeric features to predict the churn of a customer"
            df_features=spark.createDataFrame(df_raw) # If the dataframe type is Pandas
            fs_create_table(df_features=df_features, database_name=database_name, feature_table_name=feature_table_name, primary_keys=primary_keys, description=description)
    """

    from databricks.feature_store import FeatureStoreClient
    fs = FeatureStoreClient()

    feature_table = fs.create_table(name=f"{database_name}.{feature_table_name}", primary_keys=primary_keys, df=df_features, description=description)


def fs_update_feature_table(df_features:pyspark.sql.DataFrame, database_name:str, feature_table_name:str):
    """
        Update Feature Table
        
        Params:
            1. df_features: The data that will be load into a exists feature table
            2. database_name: The name of database where we want to store the feature store
            3. feature_table_name: The name of table where we want to store the feature store
            
        Use example:
            fs_update_feature_table(df_features=df_teste, database_name='fs_ecommerce', feature_table_name='customers_features_test')
    """
    
    from databricks.feature_store import FeatureStoreClient
    fs = FeatureStoreClient()

    fs.write_table(name=f"{database_name}.{feature_table_name}", df=df_features, mode="merge")
    

def read_table(database_name:str, feature_table_name:str):
    """
        Read Table: Data Lake and Feature Store
            
        Use example:
            read_table(database_name="fs_ecommerce", feature_table_name="customers_features_test")
    """
    return spark.read.table(f"{database_name}.{feature_table_name}")

