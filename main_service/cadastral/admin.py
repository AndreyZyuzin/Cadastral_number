from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import Group, User

from cadastral.models import Query

tz = timezone.get_default_timezone()


class QueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cadastral_number', 'latitude', 'longitude',
                    'get_time_came', 'result_response', 'get_time_went')
    list_display_links = list_display
    fields = ('cadastral_number', 'latitude', 'longitude',
              'time_came', 'result_response', 'time_went',)

    def get_time_came(self, query):
        return query.time_came.astimezone(tz).strftime('%Y %B %d %H:%M:%S.%f')
    get_time_came.short_description = 'Время in'

    def get_time_went(self, query):
        if not query.time_went:
            return None
        return query.time_went.astimezone(tz).strftime('%Y %B %d %H:%M:%S.%f')
    get_time_went.short_description = 'Время out'



admin.site.register(Query, QueryAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)
