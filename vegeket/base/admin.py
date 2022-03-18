from django.contrib import admin
from base.models import Item, Category, Tag
from django.contrib.auth.models import Group


# modify admin sites
class TagInline(admin.TabularInline):
    model = Item.tags.through


class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']

# show models bellow in /admin
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)

# making Group model invisible
admin.site.unregister(Group)