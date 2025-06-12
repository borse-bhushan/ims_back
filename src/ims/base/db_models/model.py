"""
Base model
"""

from django.db import models


class BaseModel(models.Model):
    """
    Base abstract model which is having the common field.
    """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    tenant_id = models.CharField(max_length=128, null=True, default=None)

    created_by = models.CharField(max_length=128, null=True, default=None)
    updated_by = models.CharField(max_length=128, null=True, default=None)

    updated_dtm = models.DateTimeField(auto_now=True)
    created_dtm = models.DateTimeField(auto_now_add=True)
    deleted_dtm = models.DateTimeField(null=True, default=None)

    class Meta:
        """
        Base model meta class
        """

        abstract = True

    migrate_to_tenant = True
