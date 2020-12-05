from django.shortcuts import render
from django.views.generic import TemplateView
from . models import *

class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('-create_at')[:7]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'author': article.author,
                'create_at': article.create_at.day,
                'description': article.description,
            })
        context = {
            'article_data': article_data,
        }
        return render(request, 'index.html', context)