from django.shortcuts import render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from link_sqlserver.models import Children, BodyCondition
from datetime import datetime, date, time
from django.utils.timezone import localtime


# Create your views here.
class ChildrenListView(ListView):
    model = Children
    context_object_name = 'object_list'
    # template_name = 'children_list.html'


class ChildrenDetailView(DetailView):
    model = Children
    context_object_name = 'object'
    dtnow = datetime.now(tz='UTC')
    dtbirth = model.birthday
    # datetime.combine(model.birthday, time=datetime.time())
    timespan = localtime(dtnow) - localtime(dtbirth)
    print(timespan)


class ChildrenCreateView(CreateView):
    model = Children
    fields = '__all__'
    success_url = reverse_lazy('childrenlist')
