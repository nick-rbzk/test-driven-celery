from celery import shared_task

@shared_task(name="print_message_main")
def print_message(message, *args, **kwargs):
    print(f"AND THE MESSAGE IS {message}")