from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy 
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify #returns slugify string

class User(AbstractBaseUser,  PermissionsMixin):
    name = models.CharField(gettext_lazy ('name'), max_length = 100)
    email = models.CharField(gettext_lazy('email address'),unique = True, max_length =100)
    username = models.CharField

class Question_paper(models.Model):
    name = models.CharField(max_length=50)    
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ["created",]
    
    def __str__(self):
        return self.name

class Question(models.Model):
    Question_paper = models.ForeignKey(Question_paper, on_delete=models.CASCADE)
    label =models.CharField(max_length=100)
    img = models.ImageField(upload_to='img_question', default='',blank=True)

    def __str__(self):    
            return self.label


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Question_paper = models.ForeignKey(Question_paper, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=None, null=True)
    
    def __str__(self):
        return self.user.email
            
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True,null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.text

class Student_answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True)
        
# for slug field in question_paper model---
@receiver(pre_save, sender = Question_paper)
def question_paper_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)


