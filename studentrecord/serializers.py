from rest_framework import serializers

from .models import Studentrecord

class StudentrecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studentrecord
        #fields = ['Id','RollNo','Name', 'Maths', 'Physics', 'Chemistry', 'Total', 'Percentage']
        fields ='__all__'