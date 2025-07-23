import pandas as pd
import sqlite3
import os

def create_db():
    os.makedirs("db", exist_ok=True)
    conn = sqlite3.connect("db/agent_ecommerce.db")

    df1 = pd.read_csv("data/Eligibility.csv")
    df2 = pd.read_csv("data/Ad Sales.csv")
    df3 = pd.read_csv("data/Total Sales.csv")

    df1.to_sql("eligibility", conn, if_exists="replace", index=False)
    df2.to_sql("ad_sales", conn, if_exists="replace", index=False)
    df3.to_sql("total_sales", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect("db/agent_ecommerce.db")
