from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Visit(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()
    next_followup = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Visit to {self.doctor.name} on {self.date}"
