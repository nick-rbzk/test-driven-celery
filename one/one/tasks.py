from celery import shared_task


@shared_task(name = "print_msg_second")
def print_message_again(message, *args, **kwargs):
  print(f"Celery is working!! Message is {message}")
