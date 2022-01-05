from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Health
from django.views.generic import CreateView, ListView
from .forms import HealthForm
from .permissions import BelongsToGroup



class ListHealthView(LoginRequiredMixin, ListView):
    model = Health
    template_name = 'health_observation/list_health_view.html'
    context_object_name = 'health_list'

    def get_queryset(self):
        """
           A base view for displaying a list of objects from current logged user except Admin.
        """
        user = self.request.user
        group = BelongsToGroup.list_group(self, user)
        if "Admin" in group:
            return self.model.objects.filter()
        return self.model.objects.filter(user=self.request.user)


class CreateHealthView(LoginRequiredMixin, CreateView):
    model = Health
    form_class = HealthForm
    template_name = 'health_observation/add_health.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('health_observation:health_add')
