from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    
    list_display = ("title","description","completed")
    
    # def completed(self,obj):
    #     return obj.is_completed == 1
    
    # completed.boolean = True
    
    # def make_completed(modeladmin, request, queryset):
    #     queryset.update(is_completed = 1)
    #     messages.success(request,"selected record(s) Marked as Completed Successfully")
    
      
admin.site.register(Todo,TodoAdmin)