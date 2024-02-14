from django.apps import AppConfig
from search.ucsb_api import populate_courses_db

class SearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "search"

    # populate the static databases
    def ready(self):
        populate_courses_db()
