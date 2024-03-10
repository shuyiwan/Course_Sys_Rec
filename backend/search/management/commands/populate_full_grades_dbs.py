import csv
from django.core.management.base import BaseCommand
from search.models import FullGrade

class Command(BaseCommand):
    help = 'Populate full_grades model from CSV'

    def handle(self, *args, **options):
        i = 0
        with open('full_grades.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                _, created = FullGrade.objects.get_or_create(
                    # Map CSV fields to model fields
                    quarter=row[0],
                    course_level=row[1],
                    course=row[2].replace(" ", ""),
                    instructor=row[3],
                    grade=row[4],
                    student_count=int(row[5])
                )
                if i % 1000 == 0:
                    print(f"Processed {i} rows")
                i += 1
        self.stdout.write(self.style.SUCCESS('Successfully populated full_grades from CSV'))
