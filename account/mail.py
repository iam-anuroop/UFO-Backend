from django.core.mail import send_mail, BadHeaderError
from decouple import config

def send_email(email=None, password=None, message=None, subject=None):
    try:
        mail_subject = subject
        message = f"Your password is {password}"
        to_email = email
        from_email=config('EMAIL_HOST_USER')
        send_mail(mail_subject, message, from_email, [to_email], fail_silently=False)
        return "done"
    except BadHeaderError as e:
        print(f"BadHeaderError: {str(e)}")
        return "error"
    except Exception as e:
        print(f"Error: {str(e)}")
        return "error"
