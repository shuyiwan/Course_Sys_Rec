from django.core.management.base import BaseCommand, CommandError
from search.ucsb_api import fetch_all_courses

class Command(BaseCommand):
    help = "Fetches all course information from the UCSB API"

    def handle(self, *args, **options):
        fetch_all_courses()