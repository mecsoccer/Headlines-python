from django.http import HttpResponse
from django.template import loader
from .models import Source, Country
from . import newsconnect


def index(request):
    template = loader.get_template("news/index.html")
    articles = newsconnect.country_headlines('ng')
    context = {'articles': articles['articles']}
    return HttpResponse(template.render(context, request))


def sources_list(request):
    template = loader.get_template("news/sources_list.html")
    sources_response = Source.objects.all()
    context = {'list_of_sources': sources_response}
    return HttpResponse(template.render(context, request))


def countries_list(request):
    template = loader.get_template("news/countries_list.html")
    countries_response = Country.objects.all()
    context = {'list_of_countries': countries_response}
    return HttpResponse(template.render(context, request))


def source_news(request, source):
    template = loader.get_template("news/index.html")
    articles = newsconnect.specific_source(source)
    context = {'articles': articles['articles'], 'source': source}
    return HttpResponse(template.render(context, request))


def country_news(request, country):
    template = loader.get_template("news/index.html")
    articles = newsconnect.country_headlines(country)
    context = {'articles': articles['articles'], 'country': country}
    return HttpResponse(template.render(context, request))


def category_news(request):
    template = loader.get_template("news/categories.html")
    articles = newsconnect.specific_source("business")
    context = {'articles': articles['articles']}
    return HttpResponse(template.render(context, request))


def about_news(request):
    template = loader.get_template("news/abouts.html")
    articles = newsconnect.specific_source("trump")
    context = {'articles': articles['articles']}
    return HttpResponse(template.render(context, request))
