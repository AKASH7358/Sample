import streamlit as st
import psycopg2  # or any other PostgreSQL library you use

# Access the secrets
db_config = st.secrets["connections.postgresql"]

# Establish the connection
conn = psycopg2.connect(
    dbname=db_config["database"],
    user=db_config["username"],
    password=db_config["password"],
    host=db_config["host"],
    port=db_config["port"]
)

# Create a cursor object
cur = conn.cursor()

# Perform query
cur.execute('SELECT * FROM mytable;')
rows = cur.fetchall()

# Print results
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

# Close the cursor and connection
cur.close()
conn.close()
