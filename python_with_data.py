# Snippet 1.
# This code is used if you need to load large datasets and compress it before loading.

# The benefits of using Parquet files include faster access to data, encoding efficiency, schema evolution support, and interoperability with various big data processing frameworks like Hadoop and Spark

###
# Resource: 
# 	https://blog.enterprisedna.co/pandas-read-parquet-file-into-dataframe/
# 	https://stackoverflow.com/questions/33813815/how-to-read-a-parquet-file-into-pandas-dataframe#47036357
###

# Export as a parquet file
df.to_parquet('dataset_name.parquet.brotli',compression='brotli')

# Read Parquet file
df = pd.read_parquet('df.parquet.brotli')

# Get file size
print ("Parquet file size:", path.getsize('dataset_name.parquet'))
print("CSV file size:", path.getsize('dataset_name.csv'))


######################################################################################################################################

# Snippet 2.

# This code is used to view categorical data in a correct order [e.g. Months in a correct order].
# Resource: Matt Harrison

dataset_name.sample(500).assign(month name=lambda df: pd.to_datetime (df['Date']).dt.month_name()
			.astype('category')
			.cat.reorder_categories(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True))
			.pipe(lambda df: pd.crosstab(index=df['Primary Type'], columns=df.month_name))
			


######################################################################################################################################








