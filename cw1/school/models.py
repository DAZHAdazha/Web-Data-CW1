from django.db import models

# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=50)
    # UDI = brief name + number
    UID = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return ''+ self.UID +',' +self.name

class Module(models.Model):
    # UID = Code + Year + Semester
    UID = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    semester = models.IntegerField()
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        return   self.code + ',' + self.name + ',' + str(self.year) + ',' + str(self.semester) + ',' + f"{[professor for professor in self.professors.all()]}"


class Rating(models.Model):
    username = models.CharField(max_length=30)
    professor_uid = models.CharField(max_length=20)
    rating = models.FloatField()
    code = models.CharField(max_length=20)
    year = models.IntegerField()
    semester = models.IntegerField()

    def __str__(self):
        return  self.username +',' +self.professor_uid + ',' + str(self.rating) +',' + self.code + ',' + str(self.year) + ',' + str(self.semester)


class User(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.username +',' +self.email + ',' + self.password

