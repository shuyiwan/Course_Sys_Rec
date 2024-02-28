from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from search import validators


class Professor(models.Model):
    fullname = models.CharField(max_length=70)
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    rating = models.FloatField()
    num_ratings = models.IntegerField()
    difficulty = models.FloatField()
    would_take_again = models.CharField(max_length=30)

    def __str__(self):
        return f"professor={self.fullname}, department={self.department}, rating={self.rating}"

class CachedCourses(models.Model):
    instructor = models.ForeignKey(Professor, on_delete=models.SET_NULL, related_name='courses', null=True)
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