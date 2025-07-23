# # app/main.py
# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from . import db, agent, query

# app = FastAPI()

# class QuestionRequest(BaseModel):
#     question: str

# @app.on_event("startup")
# def startup_event():
#     db.create_db()

# @app.post("/ask")
# def ask_question(payload: QuestionRequest):
#     sql = agent.generate_sql_query(payload.question)
#     result = query.run_query(sql)
#     return {
#         "question": payload.question,
#         "generated_sql": sql,
#         "result": result
#     }

# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from . import db, agent, query

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    db.create_db()

@app.post("/ask")
def ask_question(payload: QuestionRequest):
    sql = agent.generate_sql_query(payload.question)
    result = query.run_query(sql)
    return {
        "question": payload.question,
        "generated_sql": sql,
        "result": result
    }
