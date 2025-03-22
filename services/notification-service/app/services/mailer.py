from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.core.config import config
from app.core.logger import logger
from app.db.database import get_user_details

conf = ConnectionConfig(
    MAIL_USERNAME=config.MAIL_USERNAME,
    MAIL_PASSWORD=config.MAIL_PASSWORD,
    MAIL_FROM=config.MAIL_FROM,
    MAIL_PORT=config.MAIL_PORT,
    MAIL_SERVER=config.MAIL_SERVER,
    MAIL_STARTTLS=True,  
    MAIL_SSL_TLS=False, 
    USE_CREDENTIALS=True
)

async def send_email(user_id: int, symbol: str, price: float):
    """Send an email notification to the user"""
    try:
        user = await get_user_details(user_id)
        email_to = user.email
        subject = f"Stock Alert: {symbol}"
        body = f"<p>Stock <strong>{symbol}</strong> is at price <strong>${price}</strong></p>"

        message = MessageSchema(
            subject=subject,
            recipients=[email_to],
            body=body,
            subtype="html"
        )

        logger.info(f"Sending email to {email_to} for {symbol} at ${price}")

        fm = FastMail(conf)  
        await fm.send_message(message)  

        logger.info(f"Email successfully sent to {email_to}")

    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
        raise e
