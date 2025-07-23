# AI-Agent-for-E-commerce-questions using Ollama-tinyllama LLM

/data csv files used for this repo

/db/agent_ecommerce.db database to hold 3 SQL tables

/scripts/db.py to convert csv files into SQL Tables using SQlite
/scripts/agent.py to access the LLM and prompting to get the SQL query for user given question
/scripts/query.py to run the SQL query
/scripts/main.py uses FastAPI to receive and respond to questions
