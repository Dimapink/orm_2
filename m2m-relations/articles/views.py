from django.views.generic import ListView

from articles.models import Article, Tag


class ArticleList(ListView):
    template_name =  'articles/news.html'
    def get_queryset(self):
        return Article.objects.all().prefetch_related("scopes")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def articles_list(request):
#     template = 'articles/news.html'
#     context = {}
#
#     # используйте этот параметр для упорядочивания результатов
#     # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#     ordering = '-published_at'
#
#     return render(request, template, context)
