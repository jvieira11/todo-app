from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database import (
    listar_tarefas,
    criar_tarefa,
    atualizar_tarefa,
    concluir_tarefa,
    deletar_tarefa,
    buscar_tarefa
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    tarefas = listar_tarefas()
    return templates.TemplateResponse("index.html", {
        "request": request, "tarefas": tarefas
    })

@app.post("/criar")
async def criar(titulo: str = Form(...), descricao: str = Form("")):
    criar_tarefa(titulo, descricao)
    return RedirectResponse("/", status_code=303)


@app.post("/concluir/{id}")
async def concluir(id: int):
    concluir_tarefa(id)
    return RedirectResponse("/", status_code=303)


@app.get("/editar/{id}", response_class=HTMLResponse)
async def editar_form(request: Request, id: int):
    tarefa = buscar_tarefa(id)
    return templates.TemplateResponse(request, "index.html", {
        "tarefas": listar_tarefas(),
        "editando": tarefa
    })


@app.post("/editar/{id}")
async def editar(id: int, titulo: str = Form(...), descricao: str = Form("")):
    atualizar_tarefa(id, titulo, descricao)
    return RedirectResponse("/", status_code=303)


@app.post("/deletar/{id}")
async def deletar(id: int):
    deletar_tarefa(id)
    return RedirectResponse("/", status_code=303)