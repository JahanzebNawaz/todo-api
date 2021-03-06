from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AbstractMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

DONE = 'DONE'
NOT_DONE = 'NOTDONE'

STATUS_OPTIONS = (
    (DONE, 'DONE'),
    (NOT_DONE, 'NOT DONE'),
)


class Todo(AbstractMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    completed = models.CharField(max_length=25, choices=STATUS_OPTIONS, default=NOT_DONE)

    class Meta:
        verbose_name = 'TODO'
        ordering = ('updated',)
    
    def __str__(self):
        return self.description