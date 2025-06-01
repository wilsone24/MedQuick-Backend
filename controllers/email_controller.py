# controllers/email_controller.py

import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from sqlalchemy.orm import Session
import os
from models.user_model import User

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(subject: str, body: str, db: Session, user_id: int):
    # Obtener el usuario por ID
    user = db.query(User).filter(User.id_user == user_id).first()

    if not user or not user.email:
        print("Usuario no encontrado o sin correo electrónico.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = user.email
    msg.set_content(body)

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
