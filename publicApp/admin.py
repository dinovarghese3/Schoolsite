from django.contrib import admin

# Register your models here.
from publicApp.models import *

admin.site.register(tbl_login)
admin.site.register(tbl_teachers)
admin.site.register(tbl_student)
admin.site.register(tbl_questin)
admin.site.register(tbl_answers)
admin.site.register(tbl_message)
admin.site.register(tbl_contact)