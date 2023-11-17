from django.contrib import admin
from .models import Post, Task, Subtask

from django.contrib.auth.models import Group # J'importe pour suprrmier groupes de la page admin

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'date_posted', 'deadline','author', 'collaborators')

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'status')

class SubtaskAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'status')

admin.site.register(Post, PostAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask, SubtaskAdmin)

admin.site.unregister(Group)    # Enleve group dans l'interface d'administration

admin.site.site_header = 'HelbManager2022'
admin.site.site_title = 'HelbManager2022'

