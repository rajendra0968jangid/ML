import pandas as pd
import mysql.connector
from sklearn.linear_model import LinearRegression

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="house_db"
)

# Read SQL table
query = "SELECT avg_income, house_age, num_rooms, price FROM houses"

df = pd.read_sql(query, conn)

print(df.head())

# Features (X)
X = df[['avg_income', 'house_age', 'num_rooms']]

# Target (y)
y = df['price']

# Train model
model = LinearRegression()
model.fit(X, y)

print("Model Trained")
