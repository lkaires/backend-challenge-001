"""
Model helper
"""
###
# Libraries
###
from django.db import models


###
# Helpers
###
class TimestampModel(models.Model):
    '''
        Extend this model if you wish to have automatically updated
        created_at and updated_at fields.
    '''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)

class BaseInfoModel (TimestampModel):
    """
        Extend this model to have basic info
        Orders by update
    """
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    author = models.ForeignKey(
        'accounts.user',
        related_name='%(class)s',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ["-updated_at"]