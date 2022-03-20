from base.forms import UserCreationForm
from django.contrib import admin
from base.models import Item, Category, Tag, User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from base.models.account_models import Profile


# modify admin sites
class TagInline(admin.TabularInline):
    model = Item.tags.through


class ItemAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags']
    
    
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    
    
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
    
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
    
    add_fieldsets = (
        (None, {'fields': ('usename', 'email', 'is_active',)}),
    )
    
    add_form = UserCreationForm
    
    inlines = (ProfileInline,)


# show models bellow in /admin
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(User, CustomUserAdmin)

# making Group model invisible
admin.site.unregister(Group)