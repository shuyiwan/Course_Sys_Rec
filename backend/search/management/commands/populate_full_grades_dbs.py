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

            rowsToAdd = []
            for row in reader:
                processedRow = FullGrade(
                    quarter=row[0],
                    course_level=row[1],
                    course=row[2].replace(" ", ""),
                    instructor=row[3],
                    grade=row[4],
                    student_count=int(row[5])
                )

                # Add the row to the list of rows to add
                rowsToAdd.append(processedRow)

                # Do a single mysql insert
                if i % 1000 == 0:
                    FullGrade.objects.bulk_create(rowsToAdd)
                    print(f"Processed {i} rows")
                    rowsToAdd = []
                i += 1
            
            # Add the remaining rows
            if len(rowsToAdd) > 0:
                FullGrade.objects.bulk_create(rowsToAdd)
                print(f"Processed {i} rows")
                rowsToAdd = []
        self.stdout.write(self.style.SUCCESS('Successfully populated full_grades from CSV'))
