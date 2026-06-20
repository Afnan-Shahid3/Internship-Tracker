from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length= 100)
    website = models.URLField(blank = True)
    location = models.CharField(max_length=100, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name



class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Reviewing'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name= 'applications')
    position = models.CharField(max_length= 100)
    date_applied = models.DateField()
    status = models.CharField(max_length= 20, choices = STATUS_CHOICES)
    notes = models.TextField(blank = True)

    def __str__(self):
        return self.company.name


class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interview')
    interview_date = models.DateTimeField()
    round_name = models.CharField(max_length=50)
    feedback = models.TextField(blank = True)


    def __str__(self):
        return self.application.company.name

class Contact(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='contacts'
    )

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)

def __str__(self):
        return self.company.name
