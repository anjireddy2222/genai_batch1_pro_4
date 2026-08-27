from fastapi import APIRouter
from models.support_msg_request import SupportMsgRequest
from config.settings import settings
from config.llm_config import AiAgent
from services.support_service import SupportService

support_router = APIRouter()
support_service = SupportService()


@support_router.post("/support/msg")
def support_msg(req : SupportMsgRequest):

    ai_response = support_service.handle_support_chat(req)

    return { "status": "success", "message": "chat api endpoint", "data": ai_response }


