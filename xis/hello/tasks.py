from celery import shared_task

@shared_task(name="print_message")
def print_m(message, *args, **kwargs):
    print(f"The message is ::::{message}")