from django.views.generic import ListView
from discussion.models import Discussion, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class IndexView(LoginRequiredMixin, ListView):
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

    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        discussion_id = request.POST.get('discussion_id')
        if comment and discussion_id:
            Comment.objects.create(**{
                'discussion_id': discussion_id,
                'message': comment,
                'user_id': request.user.id
            })

        return HttpResponseRedirect('/')