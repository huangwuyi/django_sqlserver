from django.shortcuts import render,resolve_url
from django.urls import reverse,reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from link_sqlserver.models import Children,BodyCondition


# Create your views here.
class ChildrenListView(ListView):
    model = Children
    context_object_name = 'object_list'
    # template_name = 'children_list.html'


class ChildrenDetailView(DetailView):
    model = Children
    context_object_name = 'object'


class ChildrenCreateView(CreateView):
    model = Children
    fields = '__all__'
    success_url = reverse_lazy('childrenlist')

