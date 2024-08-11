import streamlit as st
import psycopg2

# Check if the key exists
if [connections.postgresql] not in st.secrets:
    st.error("PostgreSQL secrets are missing.")
else:
    # Access the secrets
    db_config = st.secrets[connections.postgresql]

    # Establish the connection
    try:
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

    except Exception as e:
        st.error(f"Error: {e}")
