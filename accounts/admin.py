from django.contrib import admin

# Register your models here.

#after migrate we still cant see table so...

from .models import User
from .models import Menu
from .models import Order
from .models import ClubMember
from .models import ClubOrder


admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(ClubMember)
admin.site.register(ClubOrder)
