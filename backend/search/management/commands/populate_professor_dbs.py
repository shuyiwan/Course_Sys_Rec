from django.core.management.base import BaseCommand, CommandError
from search.cache_prof import fetch_all_professors

class Command(BaseCommand):
    help = "Fetches all professors ratings using the RateMyProfessorAPI package"

    def handle(self, *args, **options):
        fetch_all_professors()