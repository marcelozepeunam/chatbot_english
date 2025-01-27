from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    # Por ahora, solo imprime el mensaje recibido
    print(data)
    return {"ok": True}
