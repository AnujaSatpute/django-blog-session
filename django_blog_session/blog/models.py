from django.utils import timezone
from django.db import models
from users.models import  User



class Blog(models.Model) :


    Status_Choice =(
        ('DRAFT', 'Draft'),
        ('PUBLISHED','Published')
    )

    title = models.CharField(max_length=20, null=False, blank=False)
    content =models.TextField(null=False, blank=False)
    user_id = models.ForeignKey(User, null=False,blank=False, on_delete=models.CASCADE)
    status =models.CharField(max_length=10, null=False, blank=False, choices=Status_Choice, default='DRAFT')
    created_at =models.TimeField(auto_now=timezone.now)
    updated_at = models.TimeField(auto_now=timezone.now)
