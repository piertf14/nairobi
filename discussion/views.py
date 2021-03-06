import json
import unicodedata

import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from googletrans import Translator
from pytz import unicode

from discussion.models import Discussion, Comment
from discussion.nlp.classifiers import evaluate_sentence


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

    @staticmethod
    def remove_accents(comment):
        s = ''.join((c for c in unicodedata.normalize(
            'NFD', unicode(comment)) if unicodedata.category(c) != 'Mn'))
        return s

    @staticmethod
    def translator_message(message):
        translator = Translator()
        _text = translator.translate(message, src='es')
        return _text

    def get_word_type(self, comment):
        try:
            comment = self.remove_accents(comment)
            return evaluate_sentence(comment) or False
        except Exception as e:
            return False

    def text_processing(self, comment):
        try:
            comment = self.translator_message(comment)
            url = settings.URL
            payload = {
                'text': comment.text
            }
            response = requests.request("POST", url, data=payload)
            if response.status_code == 200:
                data = json.loads(response.text)
                if data['label'] == 'neg':
                    return False
                else:
                    return True
            return evaluate_sentence(comment) or False
        except Exception as e:
            return False

    def post(self, request, *args, **kwargs):
        comment = request.POST.get('comment')
        discussion_id = request.POST.get('discussion_id')
        is_active = self.get_word_type(comment)

        if comment and discussion_id:
            Comment.objects.create(**{
                'discussion_id': discussion_id,
                'message': comment,
                'user_id': request.user.id,
                'is_active': is_active
            })

        return HttpResponseRedirect('/')
