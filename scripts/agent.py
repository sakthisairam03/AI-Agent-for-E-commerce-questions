# # app/agent.py
# import requests
# import re

# OLLAMA_URL = "http://localhost:11434/api/generate"

# SYSTEM_PROMPT = """
# You are a backend SQL assistant. Given a natural language question, you must return only a valid SQLite SQL query — nothing else.

# IMPORTANT RULES:
# - Do NOT include explanations or comments.
# - Do NOT include markdown (like ```sql).
# - Do NOT use unsupported SQL functions like DATEADD or @params.
# - Use correct table names: Eligibility, Ad Sales, Total Sales.

# Database schema:
# Table: Eligibility(eligibility_datetime_utc, item_id, eligibility_message)
# Table: Ad Sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
# Table: Total Sales(date, item_id, total_sales, total_units_ordered)

# Example: To find top-selling products last month, query from 'Total Sales' and order by 'Total Sales'.

# ONLY return the SQL query. NO explanation or commentary.
# Only respond with raw SQL (no explanations, no markdown).
# """

# def extract_sql(text):
#     match = re.search(r"(SELECT|INSERT|UPDATE|DELETE)\s.+?;", text, re.IGNORECASE | re.DOTALL)
#     if match:
#         return match.group(0).strip()
#     return text.strip().split("\n")[0]


# def generate_sql_query(user_question: str):
#     prompt = f"{SYSTEM_PROMPT}\nQuestion: {user_question}\nSQL:"
#     response = requests.post(OLLAMA_URL, json={
#         "model": "tinyllama",
#         "prompt": prompt,
#         "stream": False
#     })
#     full_response = response.json()["response"]
#     # Filter out any explanation lines
#     sql_only = full_response.strip().split("\n")[0]  # first line only
#     return sql_only.strip().strip("`")

# app/agent.py
import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are a backend SQL assistant. Given a natural language question, return only a valid SQL query for SQLite.

RULES:
- Do NOT include explanations or markdown (no ```sql).
- Do NOT use unsupported SQL functions like DATEADD or @p0.
- Use only these tables:
  - eligibility(eligibility_datetime_utc, item_id, eligibility,message)
  - ad_sales(date, item_id, ad_sales, impressions, ad_spend, clicks, units_sold)
  - total_sales(date, item_id, total_sales, total_units_ordered)

Return ONLY raw SQL — one valid SELECT query. No comments, no markdown.
"""

def extract_sql(text):
    match = re.search(r"(SELECT|INSERT|UPDATE|DELETE)\s.+?;", text, re.IGNORECASE | re.DOTALL)
    return match.group(0).strip() if match else text.strip().split("\n")[0]

def generate_sql_query(user_question: str):
    prompt = f"{SYSTEM_PROMPT}\nQuestion: {user_question}\nSQL:"
    response = requests.post(OLLAMA_URL, json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    })
    full_response = response.json()["response"]
    return extract_sql(full_response)
