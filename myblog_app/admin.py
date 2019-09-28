from django.contrib import admin

# Register your models here.
# 模型可映射到后台管理
from myblog_app.models import  Event,Guest
class EventAdmin(admin.ModelAdmin):
    fields = ['name','limit','status','address','start_time']

class GuestAdmin(admin.ModelAdmin):
    fields = ['event','realname','phone','email','sign']

admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)