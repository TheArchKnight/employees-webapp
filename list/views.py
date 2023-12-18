from django.views.generic import ListView
from .models import Employee
# Create your views here.

boss = "Olive Longfellow"

class list_employees(ListView):
  model = Employee
  context_object_name = "employees"
  template_name = "list_employees.html"

  def get(self, request, *args, **kwargs):
    if 'name' in self.request.GET:
      name = self.request.GET['name']
      Employee.objects.create(name=name)
    elif 'kill' in self.request.GET:
      Employee.objects.all().delete()
      Employee.objects.create(name=boss)
    return super().get(request, *args, **kwargs)

