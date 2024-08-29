from django.views.generic import ListView
from .models import Student


class StudentsList(ListView):
    template_name = "school/students_list.html"

    def get_queryset(self):
        return Student.objects.all().order_by("group").prefetch_related("teachers")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# def students_list(request):
#     template = 'school/students_list.html'
#     context = {"object_list": Student.objects.all().order_by("group").prefetch_related("teachers")}
#     return render(request, template, context)


