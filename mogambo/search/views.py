
from django.views.generic import ListView
from SoftwareData.models import Software
from django.db.models import Q
from star_ratings.models import Rating
from Platforms.models import platform

class SearchSoftwareListView(ListView):
    model = Software

    def get_queryset(self, *arg, **kwargs):
        request = self.request
        query = request.GET.get("q")
        if query is not None:

            lookup = (Q(name__icontains=query) |
                      Q(description__icontains=query) |
                      Q(Tag__name__icontains=query) )
                      #Q(platform__platform__icontains=query))
            return Software.objects.filter(lookup).distinct()

        return Software.objects.none()

    def get_context_data(self, **kwargs):
        """
        This has been overridden to add `car` to the templates context,
        so you can use {{ car }} etc. within the template
        """
        context = super(SearchSoftwareListView, self).get_context_data(**kwargs)
        # print(context.get("object"))

        context["read_only"] = "True"
        context["star_ratings_template_name"] = "star_ratings/wid.html"
        return context
