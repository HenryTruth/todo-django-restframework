from rest_framework import serializers

from todo.models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = [
            'id',
            'title',
            'completed'
        ]
    
    def validate_title(self, value):
        if len(value)  > 100:
            raise serializers.ValidationError("This is way to shor")
        return value