from django.contrib import admin
from .models import Company, Tool, Resume, Person, Job, Course, Education

# Register your models here.
admin.site.register(Company)
admin.site.register(Tool)
admin.site.register(Resume)
admin.site.register(Person)
admin.site.register(Job)
admin.site.register(Education)
admin.site.register(Course)
