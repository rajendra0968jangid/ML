# docker pull mysql:8.0

# docker run -d \
# --name mysql_container \
# -p 3306:3306 \
# -e MYSQL_ROOT_PASSWORD=root123 \
# -e MYSQL_DATABASE=ml_db \
# -e MYSQL_USER=mluser \
# -e MYSQL_PASSWORD=mlpass123 \
# mysql:8.0




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
