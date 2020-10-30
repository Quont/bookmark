from django.shortcuts import render

# CRUD : Create, Read, Update, Delete
# List(Read)
# 클래스형 뷰(generic view), 함수형 뷰
# 웹 페이제에 접속한다. -> 페이지를 본다.
# URl을 입력 -> 웹 서버가 뷰를 찾아서 동작시킴. -> 응답
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']# 해당 모델 중에 어떤 fiedl 내용을 수정할지 정하는 것 //site name, url 수정
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #모델명_form 형태의 templates 불러옴

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')