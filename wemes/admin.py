from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Color)
admin.site.register(Type)
admin.site.register(QRCode)