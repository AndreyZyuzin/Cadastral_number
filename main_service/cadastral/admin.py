from django.contrib import admin
from django.contrib.auth.models import Group, User

from cadastral.models import Query

class QueryAdmin(admin.ModelAdmin):
    list_display = ('cadastral_number', 'latitude', 'longitude',
                    'time_came', 'result_response', 'time_went',)
    list_display_links = list_display
    fields = ('cadastral_number', 'latitude', 'longitude',
              'time_came', 'result_response', 'time_went',)


admin.site.register(Query, QueryAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
