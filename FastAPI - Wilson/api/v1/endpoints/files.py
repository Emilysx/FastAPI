from fastapi import APIRouter, Form, UploadFile, File, status, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from models.files_models import StoredFile
from sqlalchemy.future import select
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post("/")
async def create_upload_file(file: UploadFile = File(...)):

    return {"Filename": file.filename}

@router.post("/savefile/")
async def save_upload_file(file: UploadFile = File(...)):
    # Abre (ou cria) um arquivo binário em um diretório local e escreve seu conteúdo
    with open(f"api/v1/endpoints/uploads/{file.filename}", "wb") as f:
        f.write(file.file.read())  # lê e grava o conteúdo binário do arquivo

    # Retorna mensagem de sucesso
    return {"message": f"File '{file.filename}' salvo com Sucesso!"}

@router.post("/multiplefiles")
async def multiple_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}

@router.post("/upload_db")
async def upload_file_to_bd(file: UploadFile = File(...), db: AsyncSession = Depends(get_session)):
    try:
        content = await file.read()  # Lê todo o conteúdo do arquivo como bytes

        # Cria uma instância do modelo SQLAlchemy com os dados do arquivo
        novo_file = StoredFile(
            filename=file.filename,
            content_type=file.content_type,
            content=content
        )

        db.add(novo_file)
        await db.commit()

        # Atualiza o objeto com os dados persistidos (ex: id gerado)
        await db.refresh(novo_file)

        return {
            "id": novo_file.id,
            "filename": novo_file.filename,
            "content-type": novo_file.content_type
        }
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get("/downlaod/{file_id}")
async def downlaod_file(file_id: int, db: AsyncSession = Depends(get_session)):
    try: 
        query = select(StoredFile).filter(StoredFile.id == file_id)
        result = await db.execute(query)
        stored_file = result.scalar_one_or_none()

        if not stored_file:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Arquivo não encontrado")
        
        # Cria um gerador assíncrono para enviar os bytes aos poucos
        async def file_iterator(data: bytes):
            yield data

        # Retorna o arquivo como resposta de streaming (download)
        return StreamingResponse(
            file_iterator(stored_file.content),
            media_type=stored_file.content_type,
            headers={"Content-Disposition": f"attachment; filename={stored_file.filename}"}
        )
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro ao fazer download: {e}")