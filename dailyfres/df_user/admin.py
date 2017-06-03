from django.contrib import admin
from models import Entry

# Register your models here.

class BookInfoAdmid(admin.ModelAdmin):
    """"""
    list_display = ["user", "upassword", "postbox"]

admin.site.register(Entry, BookInfoAdmid)
