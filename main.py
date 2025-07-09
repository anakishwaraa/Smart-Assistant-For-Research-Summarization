from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from utils import summarize_document, answer_question, generate_logic_questions

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    summary = summarize_document(content.decode())
    return {"filename": file.filename, "summary": summary}

@app.get("/ask/")
async def ask_question(question: str):
    document_content = "..."  # Load the document content
    answer = answer_question(question, document_content)
    justification = "This is supported by paragraph 3 of section 1."
    return {"answer": answer, "justification": justification}
