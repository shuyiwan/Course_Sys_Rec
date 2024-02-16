from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from search import validators

class CachedCourses(models.Model):
    courseID = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    # 1 = Fall, 2 = Winter, 3 = Spring, 4 = Summer
    quarter = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])
    year = models.IntegerField(validators = [validators.validate_four_digit_number])
    data = models.JSONField()

    # all rows must be unique
    class Meta:
        unique_together = ('courseID', 'quarter', 'year')

    def __str__(self):
        return f"course={self.courseID}, department={self.department}, quarter={self.quarter}, year={self.year}"