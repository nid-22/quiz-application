from django.contrib import admin
from django.urls import path,include, re_path
from . import API_views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    path('questionpaperlist/', v.question_paper_list.as_view()),
    re_path(r'questionpaper/(?P<slug>[\w\-]+)/$', v.question_paper_detail.as_view())
]
