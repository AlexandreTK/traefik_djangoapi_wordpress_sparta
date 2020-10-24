from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import UserLicense


# class UserLicenseAdmin(admin.ModelAdmin):
class UserLicenseAdmin(ImportExportModelAdmin):
    class Meta:
        model = UserLicense


    list_display = ('user_name', 'user_email', 'account_number', 'account_type', 'expiration_date', 'user_status', 'updated_at')
    
    search_fields = ('user_name', 'user_email', 'account_number')



admin.site.register(UserLicense, UserLicenseAdmin)

