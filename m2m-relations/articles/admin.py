from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_main = False
        has_duplicates = False

        added = set()
        for form in self.cleaned_data:
            if form:
                name = form.get("tag")
                if name in added:
                    has_duplicates = True
                    break
                added.add(name)

                if form.get("is_main") is True:
                    if has_main is True:
                        raise ValidationError("Основным может быть только один раздел")
                    has_main = True

        if has_duplicates is True:
            raise ValidationError("Нельзя указывать одинаковые разделы")

        if has_main is False:
            raise ValidationError("Укажите основной раздел")

        return super().clean()



class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass



