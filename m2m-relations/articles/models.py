from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scope = models.ManyToManyField("Tag", verbose_name="Тематика статьи", through="Scope")

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey("Article", on_delete=models.CASCADE, related_name="scopes", verbose_name="Статья")
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, verbose_name="Раздел", related_name="tag")
    is_main = models.BooleanField(default=False, verbose_name="ОСНОВНОЙ")

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'
        ordering = ['-is_main']


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name="Название")

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематики'
        ordering = ['name']

    def __str__(self):
        return self.name