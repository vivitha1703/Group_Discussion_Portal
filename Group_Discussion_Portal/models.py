from django.db import models

class Student(models.Model):
    batch = models.CharField(max_length=50, null=True, blank=True)  # Batch field (varchar(50))
    name = models.CharField(max_length=100, null=True, blank=True)  # Name field (varchar(100))
    roll_no = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Roll Number (varchar(20)), unique
    email_id = models.EmailField(max_length=100, unique=True, null=True, blank=True)  # Email field (varchar(100)), unique

    def __str__(self):
        return f"{self.name} - {self.batch}"

    class Meta:
        db_table = 'student'  

class SelfIntro(models.Model):
    batch = models.CharField(max_length=10, verbose_name="Batch")
    students_per_slot = models.IntegerField(verbose_name="Students Per Slot")
    slot_timing = models.IntegerField(verbose_name="Slot Timing (minutes)")
    faculty_venue = models.CharField(max_length=255, verbose_name="Faculty & Venue")
    event_date = models.DateField(verbose_name="Event Date")

    class Meta:
        db_table = "selfIntro"  # Explicit table name matching your MySQL table
       
    def __str__(self):
        return f"{self.batch} - {self.event_date.strftime('%Y-%m-%d')}"

class Faculty(models.Model):
    self_intro = models.ForeignKey(SelfIntro, on_delete=models.CASCADE, related_name="faculties")
    faculty_name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)

    class Meta:
        db_table = "selfIntro_faculty"  

class Evaluation(models.Model):
    event_name = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    email_id = models.EmailField()
    attended_date = models.DateField()
    overall_marks = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f"{self.student_name} - {self.event_name}"

    class Meta:
        db_table = 'evaluation'