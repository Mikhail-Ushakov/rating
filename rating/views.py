from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import SimpleForm,RateForm
from .models import Rate, Estimate

@method_decorator(login_required, 'dispatch')
class SimpleView(View):
    form_class = SimpleForm
    initial = {'foo': 'default value'}
    template_name = 'rating/form_template.html'

    def get(self, request):
        # print(request.GET, self.name)
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            Estimate.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form', form})
    
# class Foo(View):
#     name = 'wwwwo13owww'

#     def get(self, request):
#         return HttpResponse('hello man')

class RatingListView(ListView):
    model = Estimate
    context_object_name = 'rating_objects'
    paginate_by = 3
    template_name = 'rating/rate_list.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    
class RatingDetail(FormMixin, DetailView):
    model = Estimate
    template_name = 'rating/rate_detail.html'
    form_class = RateForm
    # success_url = reverse_lazy('detail', kwargs={'pk': self.request.kwargs['pk']})
    
    def get_success_url(self) -> str:
        return reverse('detail', kwargs={'pk': self.get_object().id})
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        current_user = get_user_model().objects.get(username=request.user.username)
        self.is_user = self.get_object().ra_te.all().filter(user=current_user.id).exists()
       
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['is_user'] = self.is_user
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            ocenochka = Rate(user=request.user, rating=form.cleaned_data['rating'])
            ocenochka.save()
            self.object.ra_te.add(ocenochka)
            self.object.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)