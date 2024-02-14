from django.db import models

class Cached_Courses(models.Model):
    # quarter follows YYYYQ format; Q is an integer [W = 1, S = 2, M = 3, F = 4]
    quarter = models.CharField(max_length=5)
    courseID = models.CharField(max_length=30)
    data = models.JSONField()

    # all rows must be unique
    class Meta:
        unique_together = ('courseID', 'quarter')

    def __str__(self):
        return f"{self.courseID} {self.quarter}"