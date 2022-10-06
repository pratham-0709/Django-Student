from django.db import models

class Student(models.Model):

    PRN = models.IntegerField(primary_key=True)
    stud_name= models.CharField(max_length=100)
    depth=1
    def __str__(self):

        return str(self.PRN)+"  "+self.stud_name
    
        
class Stud_details(models.Model):
     
     PRN=models.ForeignKey(Student, on_delete=models.CASCADE,related_name='students' )
     stud_address=models.CharField(max_length=200)
     stud_roll_no=models.IntegerField()
     stud_contact=models.IntegerField()
     stud_dob=models.DateField()
     
     def __str__(self):
      return str(self.PRN)

class Subject_wise_marks(models.Model):
    PRN=models.ForeignKey(Student, on_delete=models.CASCADE,related_name='subjectmarks')
    subject=models.CharField(max_length=50)
    marks=models.IntegerField()

    def __str__(self):
        return str(self.PRN)
