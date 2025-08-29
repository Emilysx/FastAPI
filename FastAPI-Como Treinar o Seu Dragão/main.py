from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import Dragoes, Personagens
from typing import Optional, Any

# Criando a aplicação FastAPI
app = FastAPI(
    title="API - Como Treinar o Seu Dragão",
    version="1.0.0",
    description="API - Como Treinar o seu Dragão - Feita com FastAPI"
)

# Criação de um banco de dados FAKE 
def fake_bd():
    try:
        print("Conectando com o Banco de Dados")
    finally:
        print("Fechando o Banco de Dados!")

# Informações dos Dragões
dragoes = {
    1: {
        "nome": "Banguela",
        "especie": "Fúria da Noite",
        "idade": 15,
        "nivel": 10,
        "treinador": "Soluço",
        "foto": "https://i.pinimg.com/1200x/9c/8f/2a/9c8f2abc37b88b95cbf4ddb7fe05f5e1.jpg"
    },

    2: {
        "nome": "Tempestade",
        "especie": "Nadder Mortal",
        "idade": 12,
        "nivel": 7,
        "treinador": "Astrid",
        "foto": "https://i.pinimg.com/1200x/89/cb/63/89cb63f4a02ca62d210c221449bc7b3f.jpg"
    },

    3: {
        "nome": "Batatão",
        "especie": "Gronckle",
        "idade": 3,
        "nivel": 4,
        "treinador": "Perna de Peixe",
        "foto": "https://i.pinimg.com/1200x/7c/f7/c5/7cf7c5d05891107d48cf4d955f227ac0.jpg"
    },

    4: {
        "nome": "Dente de Anzol",
        "especie": "Pesadelo Mostruoso",
        "idade": 6,
        "nivel": 8,
        "treinador": "Melequento",
        "foto": "https://i.pinimg.com/736x/cd/e6/49/cde6492be83c6345d943b28b4ab65d02.jpg"
    },

     5: {
        "nome": "Bafo e Arroto",
        "especie": "Zíper Arrepiante",
        "idade": 5,
        "nivel": 7,
        "treinador": "Cabeçadura e Cabeçaquente",
        "foto": "https://i.pinimg.com/736x/2a/2e/95/2a2e9562af5fb33b97e58eee5d2fe89b.jpg"
    }
}

# Informações dos Personagens
personagens = {
    1: {
        "nome": "Soluço",
        "idade": 20,
        "aliado_dragao": "Banguela",
        "foto": "https://i.pinimg.com/736x/f7/51/8b/f7518b216e57c868ee795fe3b6d5fc8d.jpg"
    },

    2: {
        "nome": "Astrid",
        "idade": 19,
        "aliado_dragao": "Tempestade",
        "foto": "https://i.pinimg.com/1200x/e3/e9/b8/e3e9b8bdbf820b3e40a08d06e2128d0e.jpg"
    },

    3: {
        "nome": "Perna de Peixe",
        "idade": 18,
        "aliado_dragao": "Batatão",
        "foto": "https://i.pinimg.com/1200x/f3/c2/50/f3c250d6f0896d39a1eb125f58b124df.jpg"
    },

    4: {
        "nome": "Melequento",
        "idade": 18,
        "aliado_dragao": "Dente de Anzol",
        "foto": "https://i.pinimg.com/736x/e9/a6/24/e9a6246393991fa9def88c435ef2e65a.jpg"
    },

    5: {
        "nome": "Cabeçadura",
        "idade": 20,
        "aliado_dragao": "Bafo e Arroto",
        "foto": "https://i.pinimg.com/736x/68/b1/9f/68b19f39f9bcc4db8c9971bd07a2934d.jpg"
    },

    6: {
        "nome": "Cabeçaquente",
        "idade": 20,
        "aliado_dragao": "Bafo e Arroto",
        "foto": "https://i.pinimg.com/736x/2d/f0/d8/2df0d83a9009032c70aa4e9556d15cd9.jpg"
    },
}

# Rota para listar os Dragões 
@app.get("/dragoes")
async def get_dragoes(db: Any = Depends(fake_bd)):
    return dragoes

# Pesquisar Dragão por ID
@app.get("/dragoes/{dragao_id}", description="Retorna um dragão com um id especifico", summary="Retorna um dragão")
async def get_dragao_por_id(dragao_id: int):
    try:
        dragao = dragoes[dragao_id]
        return dragao
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Dragão não encontado")
    

# Rota para listar os Personagens
@app.get("/personagens")
async def get_personagens(db: Any = Depends(fake_bd)):
    return personagens

# Pesquisar Personagem por ID
@app.get("/personagens/{personagem_id}", description="Retorna um personagem com um id especifico", summary="Retorna um personagem")
async def get_dragao_por_id(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontado")

# Cadastrar um Personagem #ARRUMAR
@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: Optional[Personagens] = None):
    next_id = len(personagens) + 1 
    personagens[next_id] = personagem
    del personagem.id
    return personagem



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8002, log_level="info", reload=True)