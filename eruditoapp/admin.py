from django.contrib import admin
from eruditoapp.models import Subject, Thread ,UserProfile, Comment


# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
    list_display= ('title','subject')

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(UserProfile)
admin.site.register(Comment)
