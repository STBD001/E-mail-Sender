from gamil_adapter import GmailAdapter
from Message import  WelcomeMessage


from dotenv import load_dotenv
from os import getenv

load_dotenv()

mailer=GmailAdapter(
    host='smtp.gmail.com',
    port=465,
    username=getenv('USERNAME'),
    password=getenv('PASSWORD')
)

mailer.login()

welcone=WelcomeMessage()

mailer.send_email(
    recipient_email="xxx@gmail.com",
    subject='Hello Worls',
    content=welcone.render(name='Kacper'))