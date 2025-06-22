from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.TextField()
    description = models.TextField()
    company = models.TextField()
    location = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    apply_link = models.URLField(max_length=200, null=True, blank=True)
    company_size_choice = models.CharField(
        max_length=20,
        choices=[
            ('SMALL', 'Small'),
            ('MEDIUM', 'Medium'),
            ('LARGE', 'Large'),
            ('ENTERPRISE', 'Enterprise'),
        ],
        null=True,
        blank=True
    )
    company_size_number = models.PositiveIntegerField(null=True, blank=True)
    remote = models.CharField(
        max_length=10,
        choices=[
            ('REMOTE', 'Remote'),
            ('ONSITE', 'Onsite'),
            ('HYBRID', 'Hybrid'),
        ],
        default='ONSITE',
    )

    def __str__(self):
        return f"{self.id} {self.title} at {self.company} ({self.location})"

class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
