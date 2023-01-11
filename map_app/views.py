from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from map_app.models import UserInfo, Address, Owner, MonsterList
from django.urls import reverse_lazy
from .models import UserInfo, Address, Owner, MonsterList

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignupForm
from django.contrib.auth import login

class AddressList(ListView):
    model = Address
    context_object_name = "address"

    def serch(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searchInputText = self.request.GET.get("search")
        print("aaa")
        if serchInputText:
            context["address"] = context["address"].filter(address1__icontains=searchInputText)
        else:
            print("else")
        context["search"] = searchInputText
        return context

class AddressDetail(LoginRequiredMixin, DetailView):
    model = Address
    context_object_name = "address_detail"
    
class AddressCreate(LoginRequiredMixin, CreateView):
    model = Address
    fields = "__all__"
    context_object_name = "address_create"
    success_url = reverse_lazy("address")

    def post(self, request):
        ticket = request.user.point
        ticket += 1
        update = UserInfo.objects.get(username=request.user)
        update.point = ticket
        update.save()
        return super().post(request)

class AddressUpdate(UpdateView):
    model = Address
    fields = "__all__"
    context_object_name = "address_update"
    success_url = reverse_lazy("address")

class AddressDelete(DeleteView):
    model = Address
    fields = "__all__"
    context_object_name = "address_delete"
    success_url = reverse_lazy("address")


class LoginView(LoginView):
    fields = "__all__"
    template_name = "map_app/login.html"

    def get_success_url(self):
        return reverse_lazy("address")

class RegisterUser(FormView):
    template_name = "map_app/register.html"
    form_class = SignupForm
    success_url = reverse_lazy("login")
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class MonsterInfo(ListView):
    model = Owner
    context_object_name = "monsters"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["monsters"] = context["monsters"].filter(user=self.request.user)
        return context

def random(request):
    ticket = request.user.point
    if request.method == 'POST':
        if ticket > 0:
            monster_list = MonsterList.objects.order_by('?')
            monster_list = monster_list[0]
            ticket -= 1
            update = UserInfo.objects.get(username=request.user)
            update.point = ticket
            update.save()

            context = {
                'monster_list':monster_list,
            }
            try:
                Owner.objects.create(user=request.user, monster=monster_list)
                return render(request, 'map_app/result.html', context)
            except:
                return render(request, 'map_app/duplication.html', context)
        
        else:
            return render(request, 'map_app/random.html')
    return render(request, 'map_app/random.html')
