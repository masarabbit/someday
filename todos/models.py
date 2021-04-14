from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False)   
    notes = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    target_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    user = models.ForeignKey(
    "jwt_auth.User",
    related_name="todos",
    on_delete=models.CASCADE
    )
    