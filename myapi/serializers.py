from rest_framework import serializers

from .models import Member
import time



class MemberSerializer(serializers.HyperlinkedModelSerializer):


	class Meta:
		
		time=time.strftime("%H:%M:%S")
		date=serializers.DateField("%d %b, %Y")
		model = Member
		fields = ('id_no','tz','name','time','date')



