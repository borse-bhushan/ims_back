"""
Token model for saving login session token against a user.
"""

from django.db import models

from base.db_models import BaseModel


class Token(BaseModel, models.Model):
    """
    Model to save login session token against a user.
    """

    created_dtm = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=512, primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "token"

    def to_dict(self):
        """
        Convert the Token instance to a dictionary representation.

        Returns:
            dict: Dictionary representation of the Token instance.
        """
        return {
            "token": self.token,
            "created_dtm": self.created_dtm,
        }
