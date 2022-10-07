from django.contrib import admin
from .models import hotel, room, order, client, range, show
admin.site.register(hotel)
admin.site.register(room)
admin.site.register(order)
admin.site.register(client)
admin.site.register(range)
admin.site.register(show)

