from django.shortcuts import render, resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from link_sqlserver.models import Children, BodyCondition
from datetime import datetime, date, time, timezone, timedelta
from django.utils.timezone import localtime
from django.views.generic import DetailView
from django.utils import dateparse
from getmac import get_mac_address
import socket


# Create your views here.
class ChildrenListView(ListView):
    model = Children
    context_object_name = 'object_list'
    # template_name = 'children_list.html'


class ChildrenDetailView(DetailView):
    model = Children
    context_object_name = 'object'

    # dtnow = datetime.now(tz=timezone(timedelta(hours=8)))
    # dtbirth = model.birthday
    # print(type(dtbirth))
    # extra_context =
    # datetime.combine(model.birthday, time=datetime.time())
    # timespan = dtnow - (dtbirth.astimezone(tz=timezone(timedelta(hours=8))))
    # print(timespan)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timedelta'] = self.calculate_timedelta()
        return context

    def calculate_timedelta(self):
        key = self.kwargs.get(self.pk_url_kwarg)
        b = Children.objects.get(id=key).birthday.astimezone(timezone(timedelta(hours=8)))
        print(b)
        n = datetime.now(tz=timezone(timedelta(hours=8)))
        print(n)
        print(n - b)
        return n - b


class ChildrenCreateView(CreateView):
    model = Children
    fields = '__all__'
    success_url = reverse_lazy('childrenlist')


class ChildrenUpdateView(UpdateView):
    model = Children
    fields = '__all__'
    success_url = reverse_lazy('childrenlist')


class ChildrenDeleteView(DeleteView):
    model = Children
    context_object_name = 'object'
    success_url = reverse_lazy('childrenlist')


def MacAndIP(request):
    if request.method == "POST":
        ip = socket.gethostbyname(socket.gethostname())
        # socket.gethostbyname() '10.2.42.66'
        mac = get_mac_address()
        content = {"ip": ip, "mac": mac}
    else:
        content = {}
    return render(request, template_name="IPandMac.html", context={"value": content, })
