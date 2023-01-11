from django.contrib import admin
from .models import UserInfo, Address, Owner, MonsterList

admin.site.register(UserInfo)
admin.site.register(Address)
admin.site.register(Owner)
admin.site.register(MonsterList)

# Register your models here.
