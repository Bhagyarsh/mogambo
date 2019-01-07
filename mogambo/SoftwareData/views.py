from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Software, Comment
from .forms import SoftwareForm

# Create your views here.


class SoftwareListView(ListView):
    model = Software

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(SoftwareListView, self).get_context_data(**kwargs)
        # print(context.get("object"))

        context["read_only"] = "True"
        context["star_ratings_template_name"] = "star_ratings/wid.html"
        return context


class SoftwareCreateView(CreateView):
    form_class = SoftwareForm
    model = Software
    template_name = "SoftwareData/software_form.html"
    success_url = '/'


class SoftwareDetailView(DetailView):
    queryset = Software.objects.all()

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(SoftwareDetailView, self).get_context_data(**kwargs)
        # print(context.get("object"))
        context["Comment"] = Comment.objects.filter(Software=context.get("object"))

        return context
