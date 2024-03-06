from django.core.management.base import BaseCommand, CommandError
from search.cache_prof import fetch_all_tags

class Command(BaseCommand):
    help = "Fetches all professors tags using the RateMyProfessor scraper in search/rmf_api.py"

    def handle(self, *args, **options):
        fetch_all_tags()