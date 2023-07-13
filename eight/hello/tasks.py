from celery import shared_task


@shared_task(name="print_message")
def print_msg(message, *args, **kwargs):
    print(f"HELL YEAHH. Message is {message}")

