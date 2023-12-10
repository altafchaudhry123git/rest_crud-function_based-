from rest_framework import serializers
from myapp.models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields='__all__'
        fields=('id','name', 'course', 'college','city')

