import streamlit as st

# Initialize connection.
conn = st.connection(
    "sql", 
    dialect=st.secrets["postgresql"]["dialect"],
    host=st.secrets["postgresql"]["host"],
    port=st.secrets["postgresql"]["port"],
    database=st.secrets["postgresql"]["database"],
    username=st.secrets["postgresql"]["username"],
    password=st.secrets["postgresql"]["password"]
)

# Perform query.
df = conn.query('SELECT * FROM mytable;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
