from django.contrib import admin
import nested_admin
from .models import  Question_paper,Question, Student_answer ,Answer,Student,User



class Answer_inline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4

class Question_inline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [Answer_inline,]
    extra = 1

class Question_paper_admin(nested_admin.NestedModelAdmin):
    model  =Question_paper
    inlines = [Question_inline,]

class Student_answer_inline(admin.TabularInline):
    model = Student_answer

class Student_admin(admin.ModelAdmin):
    inlines = [Student_answer_inline,]
    


# class Answer_admin(admin.ModelAdmin):    
#     list_display =[ 'question', 'mcq_question' ,'text','student']
#     list_filter = []    
# class Student_admin(admin.ModelAdmin):
#     list_display =[ 'user', 'Question_paper' ,'timestamp']
#     list_filter = []    

admin.site.register(Student,Student_admin)
admin.site.register(Question_paper,Question_paper_admin)
admin.site.register(Answer)
admin.site.register(Question)    
admin.site.register(Student_answer)




