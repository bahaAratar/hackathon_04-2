from celery import shared_task
from django.core.mail import send_mail
import time

@shared_task
def send_activation_code(email, code):
    send_mail(
        'activaion account', # title
        f'http://localhost:8000/account/activate/{code}', # body
        'dead.baha.31@gmail.com', # from
        [email] # to
    )

@shared_task
def send_reset_password_code(email, code):
    send_mail(
        'reset password', # title
        f'привет. чтобы сбросить пароль, тебе нужно знать этот код:\n{code}', # body
        'dead.baha.31@gmail.com', # from
        [email] # to
    )