from ast import Sub
from functools import partial
from re import sub
from urllib import response
from urllib.request import Request
from django.http import JsonResponse
from django.db import transaction
import student
from .models import Stud_details, Student, Subject_wise_marks
from .serializers import stud_details_serialiser, studentserializer, sub_wise_marks_serialiser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from student import serializers
from django.core.serializers import json
from django.utils.translation import gettext as _
from django.utils.translation import get_language ,activate,gettext



@transaction.atomic

@api_view(['GET','POST'])
def student_list(request):
     #get all students
     #serialize them
     # return json
     if request.method=='GET':
        stud = Student.objects.all()
        serializer= studentserializer(stud,many=True)
        return Response({'stud':serializer.data})
     
     if request.method=='POST':
          serializer= studentserializer(data= request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)     

#Update DELETE on Student table
@api_view(['PUT','PATCH','DELETE'])
def student_list_by_id(request):

     if request.method=='PUT':
          data=request.data
          serializer=studentserializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)

          return Response(serializer.errors)


     elif request.method=='PATCH':
          
          data=request.data
          obj=Student.objects.get(PRN=data['PRN'])
          serializer=studentserializer(obj, data=data, partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)

          return Response(serializer.errors)

     elif request.method=='DELETE':
          data=request.data
          obj=Student.objects.get(PRN=data['PRN'])
          obj.delete()
          return Response("Person is deleted!")

# Read Create student details
@api_view(['GET','POST'])
def stud_details1(request):
    if request.method=='GET':
     stud=Stud_details.objects.all()
     serializer=stud_details_serialiser(stud,many=True)
     return Response({'stud':serializer.data})

    if request.method=='POST':
          serializer= stud_details_serialiser(data= request.data)
          
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          
          return Response(serializer.errors)      
 

#Delete update student details
@api_view(['GET','PATCH','DELETE'])
def stud_details_update(request,prn):
     try:
          stud= Stud_details.objects.get(PRN=prn)
     except Stud_details.DoesNotExist:
          msg=_("PRN is not valid")
          return Response({'Error':msg})
                                   
     if request.method=="GET":
        serializers= stud_details_serialiser(stud,many=True)
        return Response(serializers.data)

     elif request.method=="PATCH":
          serializers = stud_details_serialiser(stud,data=request.data,partial=True)

          if serializers.is_valid()==True: 
             serializers.save()
             return Response(serializers.data)
          return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)      

     elif request.method=='DELETE':    
          stud.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)   


#Read create subject wise marks detail
@api_view(['GET','POST'])
def sub_marks_detail(request):
 try:    
      if request.method=='GET':
        stud=Subject_wise_marks.objects.all()
        serializer=sub_wise_marks_serialiser(stud,many=True)
        return Response({'stud':serializer.data})
      if request.method=='POST':
          serializer= sub_wise_marks_serialiser(data= request.data)
          if serializer.is_valid():
            serializer.save()
            
      return Response(serializer.data, status=status.HTTP_201_CREATED)
 except Exception as e:
          msg=_("This method is not allowed!!")
          return Response({'Error':msg})
                                   

 #update delete subjectwise marks details
@transaction.atomic
@api_view(['GET','PATCH','DELETE'])
def sub_marks_update(request,prn,sub):
     try:
          stud= Subject_wise_marks.objects.get(PRN=prn,subject=sub)
     except Subject_wise_marks.DoesNotExist:
          return Response({'Error':'PRN or subject is not valid'})
                                   
     if request.method=="GET":
        serializers= sub_wise_marks_serialiser(stud)
        return Response(serializers.data)

     elif request.method=="PATCH":
          serializers = sub_wise_marks_serialiser(stud,data=request.data,partial=True)

          if serializers.is_valid()==True: 
             serializers.save()
             return Response(serializers.data)
          return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)      

     elif request.method=='DELETE':    
          stud.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)  

#All details of perticular student
@api_view(['GET','POST'])
def all_details(request,prn):
     try:
          stud= Stud_details.objects.get(PRN=prn)
          stud1=Student.objects.get(PRN=prn)
          stud3=Subject_wise_marks.objects.all().filter(PRN=prn)
     except Stud_details.DoesNotExist:
          return Response({'Error':'PRN is not valid'})
                                   
     if request.method=="GET":
        serializers= stud_details_serialiser(stud)
        serializers1=studentserializer(stud1)
        serializers2=sub_wise_marks_serialiser(stud3, many=True)
        return Response({'student':serializers1.data,'student details':serializers.data,'Subjectwise marks':serializers2.data})
     
@api_view(['GET'])     
def all_details_usingRelation(request,prn):
     try:
           #a=Student.objects.prefetch_related('students','subjectmarks').filter(subjectmarks__PRN=2000, students__PRN=2000)
           #a= Student.objects.raw('select PRN,stud_roll_no from student_student,student_stud_details where student_student.PRN=2000 ')
           stud1=Stud_details.objects.select_related('PRN').filter(PRN=prn)
           stud=Subject_wise_marks.objects.select_related('PRN').filter(PRN=prn)
           
     except Stud_details.DoesNotExist:
           return Response({'Error':'PRN is not valid'})
        
     serializers2= stud_details_serialiser(stud1,many=True)
     serializers1=sub_wise_marks_serialiser(stud,many=True)
     # if request.method=="GET":
     #    for name in stud3:
     #       print(name.PRN)
     #       print(name.stud_roll_no)
     
     return Response({'student':serializers2.data,'Subjectwise marks':serializers1.data})

