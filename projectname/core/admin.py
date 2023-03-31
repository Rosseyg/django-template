from django.contrib import admin
from .models import Stylist, Member, Donation, Post
# Register your models here.
admin.site.register(Stylist)
admin.site.register(Member)
admin.site.register(Donation)
admin.site.register(Post)
