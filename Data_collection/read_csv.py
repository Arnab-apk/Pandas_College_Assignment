import pandas as pd

# Read the CSV file
df = pd.read_csv(r'c:\Users\USER\Desktop\Pandas\Data_collection\student_exam_scores.csv')

# Display the first 10 rows of the data
print("\nFirst 10 rows of the data:")
print(df.head(10))
# Display the last 10 rows of the data
print("\nLast 10 rows of the data:")
print(df.tail(10))

# Display basic information about the dataset
print("\nDataset information:")
print(df.info())

# Display basic statistical summary
print("\nStatistical summary:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

print("\ntype df")
print(type(df))

# Finding summary of dataframe columns
print("\nSummary of DataFrame columns:")
print(list(df.columns))

#transposing 5 columnas
print("\nTransposed first 5 columns:")
print(df.head().transpose())

#transposing last 5 columnas
print("\nTransposed last 5 columns:")
print(df.tail().transpose())

#dimension of dataframe
print("\nDimension of DataFrame (rows, columns):")
print(df.shape)

#slicing first 5 rows
print("\nSlicing first 5 rows:")
print(df[:40])

#slicing sleep_hours column
print("\nSlicing 'sleep_hours' column:")    
print(df['sleep_hours'][:5])

#value counts in 'exam_score' column
print("\nValue counts in 'exam_score' column:")
print(df[["sleep_hours","hours_studied","exam_score"]].value_counts(normalize=True)*100)

#cross tabulation between 'hours_studied' and 'exam_score'
print("\nCross tabulation between 'hours_studied' and 'exam_score':")
print(pd.crosstab(df['hours_studied'], df['exam_score']))

#sorting data frame by columns
print("\nDataFrame sorted by 'exam_score' and 'hours_studied':")
print(df[['exam_score', 'hours_studied']].sort_values(by=['exam_score', 'hours_studied'], ascending=[False, False]).head(10))

