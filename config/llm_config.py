from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from config.settings import settings
from langchain.agents import create_agent
from tools.external_tools import send_email
from tools.support_tools import create_ticket, get_ticket, update_ticket

class AiAgent:

    @staticmethod
    def get_ai_agent(provider = None, model=None, prompt=None):

        provider = provider or settings.DEFAULT_LLM_PROVIDER

        llm_client = ""
        if provider.lower() == "openai":
            llm_client = ChatOpenAI( model= model or settings.DEFAULT_OPENAI_MODEL, api_key=settings.OPENAI_API_KEY )

        if provider.lower() == "anthropic":
            llm_client = ChatAnthropic(model_name= model or settings.DEFAULT_ANTHROPIC_MODEL, api_key=settings.ANTHROPIC_API_KEY)

        ai_agent = create_agent( model=llm_client, system_prompt=prompt, tools=[ send_email, create_ticket, get_ticket, update_ticket ] )


        return ai_agent





