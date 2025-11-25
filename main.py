import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.models import models
from database.database import engine, SessionLocal
from datetime import date

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, message: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "message": message})


@app.post("/subscribe", response_class=RedirectResponse)
async def subscribe(
    email: str = Form(...),
    nome: str = Form(...),
    sobrenome: str = Form(...),
    telefone: str = Form(...),
    data_nascimento: date = Form(...),
    desafio: str = Form(...),
    
    db: Session = Depends(get_db),
):
    new_lead = models.Lead(
        email=email,
        nome=nome,
        sobrenome=sobrenome,
        telefone=telefone,
        data_nascimento=data_nascimento,
        desafio=desafio
    )
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return RedirectResponse(url="/?message=Inscrição realizada com sucesso!", status_code=303)


@app.get("/admin", response_class=HTMLResponse)
async def read_admin(request: Request, db: Session = Depends(get_db)):
    leads = db.query(models.Lead).all()
    return templates.TemplateResponse("admin.html", {"request": request, "leads": leads})
