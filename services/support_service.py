from models.support_msg_request import SupportMsgRequest
from config.llm_config import AiAgent
from prompts.support_prompt import support_prompt
import json

class SupportService:

    def handle_support_chat(self, req: SupportMsgRequest):
        ai_agent = AiAgent.get_ai_agent( prompt=support_prompt )

        ai_response = ai_agent.invoke({ "messages": [ { "role": "user", "content": req.model_extra } ] })
        ai_json_data = json.loads( ai_response["messages"][-1].content )

        return {  "ai_json_data": ai_json_data, "ai_response": ai_response }
