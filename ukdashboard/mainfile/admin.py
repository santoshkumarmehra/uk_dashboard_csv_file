from django.contrib import admin
from .models import UkCompany, Segment


# class AdminUkCompany(admin.ModelAdmin):
#     list_display = ['name', 'segment', 'product_type', 
#     'Estimated_Number_of_Employees', 'Total_Funding', 'Estimated_Revenue', 'Last_Funding_Date', 'Last_Funding_Type']


class AdminSegment(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(UkCompany)#, AdminUkCompany)
admin.site.register(Segment, AdminSegment)


