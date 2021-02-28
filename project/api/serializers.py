from rest_framework import serializers
from quiz.models import Question_paper,Question, Student_answer ,Answer,Student,User

class question_paper_serializer(serializers.ModelSerializer):
    class Meta:
        model = Question_paper
        fields = ['id','name','description','created','slug', ]

class Answer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class Question_serializer(serializers.ModelSerializer):
    answer_set = Answer_serializer(many = True)
    class Meta:
        model = Question
        fields = "__all__"


class question_paper_detail_serializer(serializers.ModelSerializer):
    question_set = Question_serializer(many = True)
    class Meta:
        model = Question_paper
        fields = "__all__"

class Student_answer_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_answer
        fields = "__all__"

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"




    
    
