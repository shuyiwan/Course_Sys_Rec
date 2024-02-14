from django.apps import AppConfig

class SearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "search"

    # populate the static databases
    def ready(self):
        # required to import here or it will fail due to Django starting up its databases
        from search.ucsb_api import populate_courses_db
        populate_courses_db()
