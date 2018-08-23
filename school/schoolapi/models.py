from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50,unique=True)


class Course(models.Model):
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    department_id = models.ForeignKey(Department ,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('department_id', 'name')

    def __str__(self):
        return self.name + " " + self.department_id.name
