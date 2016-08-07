# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.models import Person, CustomGroup
from django.contrib.auth.models import Group


class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('field',)

admin.site.register(CustomGroup, CustomGroupAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Person, PersonAdmin)
admin.site.unregister(Group)
