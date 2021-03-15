from django.contrib import admin
from .models import Todos


class TodosAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'is_completed', 'created_at', 'id')


admin.site.register(Todos, TodosAdmin)
