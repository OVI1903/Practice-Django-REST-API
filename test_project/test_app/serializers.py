from rest_framework import serializers
from .models import Test_member


#Serializer Class using ModelSerializer

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test_member
        fields = ['id','Member_Name','Age','Address']
        
        
"""

class TestSerializer(serializers.Serializer):
    
    Member_Name = serializers.CharField(max_length=25)
    Age = serializers.IntegerField()
    Address = serializers.CharField(max_length=25)
    
    def create(self, validated_data):
        return Test_member.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.Member_Name = validated_data.get('Member_Name', instance.Member_Name)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Address = validated_data.get('Address', instance.Address)
        
        instance.save()
        return instance

"""