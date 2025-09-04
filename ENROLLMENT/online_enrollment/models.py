from django.db import models

# Create your models here.
class Student_info(models.Model):
  id_no = models.CharField(max_length=100)
  name  = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  phone_no = models.IntegerField(max_length=10)
  dob = models.DateTimeField()

  def __str__(self):
    return f"{self.name}"

class Parrent_info(models.Model):
  mother_name = models.CharField(max_length=100)
  father_name = models.CharField(max_length=100)
  mother_contact = models.IntegerField(max_length=10)
  father_contact = models.IntegerField(max_length=10)
  guardian_name = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.mother_name}{self.father_name}"

class Course(models.Model):
  course_name = models.CharField(max_length=100)
  course_description = models.CharField(max_length=100)
  no_of_units = models.IntegerField(max_length=10)
  course_code = models.CharField(max_length=100)
  department = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.course_name}"

class Enrollment_info(models.Model):
  stud_name = models.CharField(max_length=100)
  course_n = models.CharField(max_length=100)
  date_enroll = models.DateTimeField(auto_now_add=False)
  status = models.CharField(max_length=100)
  student_type = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.stud_name}"

class Payment(models.Model):
  student = models.CharField(max_length=100)
  amount = models.IntegerField(max_length=100)
  dop = models.DateTimeField(auto_now_add=False)
  pay_method = models.CharField(max_length=100)
  pay_status = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.student}"
