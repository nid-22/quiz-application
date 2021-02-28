from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from quiz.models import Question_paper,Question, Student_answer ,Answer,Student,User
from .serializers import question_paper_serializer, question_paper_detail_serializer

class question_paper_list(generics.ListAPIView):
    queryset = Question_paper.objects.all()
    serializer_class = question_paper_serializer

class question_paper_detail(generics.RetrieveAPIView):
    serializer_class = question_paper_detail_serializer
    #permission_classes = []
    def get(self,*args,**kwargs):
        slug = self.kwargs["slug"]
        question_paper = get_object_or_404(Question_paper, slug=slug)
        stud_obj,created =Student.objects.get_or_create(user=self.request.user, Question_paper=question_paper)
        if created:
            for question_ in Question.objects.filter(Question_paper=question_paper):
                Student_answer.objects.create(student=stud_obj, question=question_)
        return Response( self.get_serializer(question_paper, context={'request':self.request}).data)
               

 
