from fastapi import APIRouter

router = APIRouter()
@router.get('/api/chat')
def chat():
    return {"message": "wo are chat now."}

@router.post('/api/image')
def chat():
    return {"message": "wo are chat now."}