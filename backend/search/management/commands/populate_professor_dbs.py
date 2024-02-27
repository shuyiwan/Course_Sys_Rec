from django.core.management.base import BaseCommand, CommandError
from search.views_helpers import fetch_all_professors

class Command(BaseCommand):
    help = "Fetches all professors from the RMF API"

    def handle(self, *args, **options):
        fetch_all_professors()