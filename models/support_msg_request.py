from pydantic import BaseModel


class SupportMsgRequest(BaseModel):
    user_id: int
    ticket_id: int
    user_message: str


