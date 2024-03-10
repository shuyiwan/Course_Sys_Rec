import csv
from django.core.management.base import BaseCommand
from search.models import FullGrade

class Command(BaseCommand):
    help = 'Populate full_grades model from CSV'

    def handle(self, *args, **options):
        with open('~/Downloads/full_grades.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                _, created = FullGrade.objects.get_or_create(
                    # Map CSV fields to model fields
                    quarter=row[0],
                    course_level=row[1],
                    course=row[2],
                    instructor=row[3],
                    grade=row[4],
                    student_count=int(row[5])
                )
        self.stdout.write(self.style.SUCCESS('Successfully populated full_grades from CSV'))
