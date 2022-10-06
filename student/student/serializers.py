import re
from datetime import date
from .models import  Student
from .models import Stud_details
from .models import Subject_wise_marks
from rest_framework import serializers


class studentserializer(serializers.ModelSerializer):
  
    class Meta:
       model=Student
       fields=['PRN','stud_name'] 

    def validate(self,data):
        special_characters= "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        if any (c in special_characters for c in data['stud_name']):
         raise serializers.ValidationError("Name should not contain any special characters")
        return data   

class stud_details_serialiser(serializers.ModelSerializer):
     
    stud_name=serializers.SerializerMethodField()

    class Meta:
        model=Stud_details
        fields=['PRN','stud_name','stud_address','stud_roll_no','stud_contact','stud_dob']
        #fields='__all__'
       
    def get_stud_name(self,obj):
        stud_obj=Student.objects.get(stud_name=obj.PRN.stud_name)
        return {stud_obj.stud_name}


    #validations starts from here
    def validate(self, data):
         # Pattern = re.compile("(0|91)?[6-9][0-9]{9}")
          b_date=data['stud_dob']
          contact=str(data['stud_contact'])
          r=re.fullmatch('[6-9][0-9]{9}',contact)
          #if (data['PRN']==" "):
           # raise serializers.ValidationError("PRN should not be empty!")
          
          if (data['stud_roll_no']<=0 or data['stud_roll_no']>=60):
               raise serializers.ValidationError("Roll number should be between 1 to 60!")         
          
          #elif (Pattern.match(contact)==False):
          elif(r==None):
                  raise serializers.ValidationError("Incorrect Contact number!!")
          elif(b_date.year!=2012 and b_date.year!=2013):
            print([b_date.year])
            raise serializers.ValidationError("Birth year should be in between 2012 to 2013")
          return data

class sub_wise_marks_serialiser(serializers.ModelSerializer):
     
     stud_name=serializers.SerializerMethodField()
     class Meta:
        model=Subject_wise_marks()
        fields=['PRN','subject','marks','stud_name']
         #fields='__all__'

     def get_stud_name(self,obj):
        stud_obj=Student.objects.get(stud_name=obj.PRN.stud_name)
        return {stud_obj.stud_name}     

      