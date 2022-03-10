import datetime

from RendezVous.celery import app


@app.task(bind=True, retry_kwargs={'countdown': 15, 'max_retries': 3})
def create_client_profile(
    self, id: str, email_confirmed: bool,
    last_name: str, first_name: str, created_at: datetime,
):
    pass
