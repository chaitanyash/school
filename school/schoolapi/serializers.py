from rest_framework import serializers
from .models import *

#Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


#Course Serializer
class CourseSerializer(serializers.ModelSerializer):

	# department_id = DepartmentSerializer(read_only=True)

	class Meta:
		many=True
		model = Course
		fields = ('id','name','duration','department_id')
		depth = 1
	# department_name = DepartmentSerializer()
