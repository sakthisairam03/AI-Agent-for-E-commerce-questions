# # app/query.py
# from .db import get_connection

# # app/query.py
# def run_query(sql: str):
#     conn = get_connection()
#     try:
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         columns = [desc[0] for desc in cur.description]
#         return {"columns": columns, "rows": rows}
#     except Exception as e:
#         return {
#             "error": str(e),
#             "invalid_sql": sql
#         }
#     finally:
#         conn.close()

# app/query.py
from .db import get_connection

def run_query(sql: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return {
            "error": str(e),
            "invalid_sql": sql
        }
    finally:
        conn.close()
