from langchain.tools import tool


@tool(description="use this tool to create support ticket")
def create_ticket():

    return "ticket created"

@tool(description="use this tool to get ticket details")
def get_ticket():

    return "ticket details"


@tool(description="use this tool to update support ticket")
def update_ticket():

    return "ticket details updated"







