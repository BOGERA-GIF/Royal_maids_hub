from django.db import models

# Create your models here.
# from django.db import models

# class Contact(models.Model):
#     full_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     gender = models.CharField(max_length=10)
#     nationality = models.CharField(max_length=100)
#     home_address = models.TextField()

#     def __str__(self):
#         return self.full_name

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=100)
    home_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    
    # Educational Background
    EDUCATION_LEVEL_CHOICES = [
        ('Primary School', 'Primary School'),
        ('Secondary School', 'Secondary School'),
        ('Vocational Training', 'Vocational Training'),
        ('Other', 'Other')
    ]
    education_level = models.CharField(max_length=50, choices=EDUCATION_LEVEL_CHOICES)
    other_education = models.CharField(max_length=100, blank=True, null=True)

    # Work Experience
    work_experience = models.BooleanField()
    work_experience_details = models.TextField(blank=True, null=True)

    # Medical Conditions or Allergies
    medical_conditions = models.BooleanField()
    medical_conditions_details = models.TextField(blank=True, null=True)

    # Training Program Preference
    TRAINING_PROGRAM_CHOICES = [
        ('Advanced Cooking', 'Advanced Cooking'),
        ('Nutrition', 'Nutrition'),
        ('Childcare & Family Management', 'Childcare & Family Management'),
        ('Laundry', 'Laundry'),
        ('Cleaning', 'Cleaning'),
        ('Gardening', 'Gardening')
    ]
    training_program = models.CharField(max_length=50, choices=TRAINING_PROGRAM_CHOICES)

    # Emergency Contact
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.full_name
