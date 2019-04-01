from django.views.generic import ListView
from discussion.models import Discussion


class IndexView(ListView):
    template_name = 'discussion/index.html'
    model = Discussion

    def get_queryset(self):
        queryset = self.model.objects.filter(is_active=True)
        return queryset

    def get_context_data(self, **kwargs):
        queryset = self.get_queryset()
        context_object_name = self.get_context_object_name(queryset)

        data = {
            'object_list': queryset
        }

        data.update(kwargs)
        if context_object_name is not None:
            data[context_object_name] = queryset
        return data