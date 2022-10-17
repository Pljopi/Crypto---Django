from django.contrib import admin
from .models import Users, Currencies, Favorites

admin.site.register(Users)
admin.site.register(Currencies)
admin.site.register(Favorites)
# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    pass
    list_display = ('username', 'password', 'email', 'id')
    readonly_fields: ('id')


admin.site.unregister(Users)
admin.site.register(Users, UsersAdmin)


class FavoritesAdmin(admin.ModelAdmin):
    pass
    list_display = ('tag', 'user_id')
    readonly_fields: ('id')


admin.site.unregister(Favorites)
admin.site.register(Favorites, FavoritesAdmin)
