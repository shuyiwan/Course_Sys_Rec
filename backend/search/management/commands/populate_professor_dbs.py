from django.core.management.base import BaseCommand, CommandError
from search.cache_prof import fetch_all_professors

class Command(BaseCommand):
    help = "Fetches all professors from the RMF API"

    def handle(self, *args, **options):
        fetch_all_professors()