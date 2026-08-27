from langchain.tools import tool


@tool(description="use this tool to send email notifications")
def send_email(from_email, to_email, subject, body ):

    return "email sent"



