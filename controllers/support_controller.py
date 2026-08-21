from fastapi import APIRouter
from models.support_msg_request import SupportMsgRequest
support_router = APIRouter()



@support_router.post("/support/msg")
def support_msg(req : SupportMsgRequest):


    return { "status": "success", "message": "chat api endpoint", "data": req }


