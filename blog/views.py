from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class IndexPage(TemplateView):

    def get(self, request, **kwargs):

        article_data = []
        all_articles = Article.objects.all().order_by('-create_at')[:9]

        for article in all_articles:
            article_data.append({
                'title': article.title,
                'cover': article.cover.url,
                'category': article.category.title,
                'author': article.author,
                'create_at': article.create_at.day,
                'create_at2': article.create_at.month,
                'description': article.description,
            })
        context = {
            'article_data': article_data,
        }
        return render(request, 'index.html', context)


class AboutPage(TemplateView):
    template_name = "about.html"


class AllArticleAPIView(APIView):

    def get(self, request, format=None):
        try:
            all_articles = Article.objects.all().order_by('-create_at')[:20]
            data = []

            for article in all_articles:
                data.append({
                    "title": article.title,
                    "cover": article.cover.url,
                    "content": article.content,
                    "category": article.category.title,
                    "author": article.author.user.first_name + ' ' + article.author.user.last_name,
                    "create_at": article.create_at.day,
                    "create_at2": article.create_at.month,
                })
            return Response({'data': data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleAPIView(APIView):

    def get(self, request, format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains=article_title)
            serialized_data = serializers.SingleArticleSerializer(article, many=True)
            data = serialized_data.data

            return Response({'data': data}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "اوه! یه مشکلی پیش اومده. سریع برطرفش میکنم :)"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
