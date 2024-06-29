from rest_framework import serializers
from .models import Form, Question, Option, Response

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'                        