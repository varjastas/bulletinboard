from django.contrib import admin
import datetime
from .models import AdvUser, SuperRubric, SubRubric, Bb, AdditionalImage
from .utilities import send_activation_notification
from .forms import SubRubricForm

class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage
    
class BbAdmin(admin.ModelAdmin) :
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'contacts', 'image', 'is_active')
    inlines = (AdditionalImageInline,)

def send_activation_notifications(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)
    modeladmin.message_user(request, 'Letters of demand have been sent')

send_activation_notifications.short_description = \
'Sending letters with activation requests'

class NonactivatedFilter(admin.SimpleListFilter):
    title = 'Have been activated?'
    parameter_name = 'actstate'
    
    def lookups(self, request, model_admin):
        return (
            ('activated', 'Passed'),
            ('threedays', 'Has been gone for more than 3 days'),
            ('week', 'Passed more than a week'),
        )
        
    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
        elif val == 'week':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False, date_joined__date__lt=d)
                   
class AdvUserAdmin(admin.ModelAdmin) :
    list_display = ('is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NonactivatedFilter,)
    fields = (('username', 'email'), ('first_name', 'last_name'),
              ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
            'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notifications,)

class SubRubricinline(admin.TabularInline):
    model = SubRubric
    form = SubRubricForm  
    
class SuperRubricAdmin (admin.ModelAdmin) :
    exclude = ('super_rubric',)
    inlines = (SubRubricinline,)
      
    
admin.site.register(AdvUser, AdvUserAdmin)  
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(Bb, BbAdmin)
admin.site.register(SubRubric)