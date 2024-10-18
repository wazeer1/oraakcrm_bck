from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True, editable=False)
    creator = models.ForeignKey(User, blank=True, null=True, editable=False,
                                related_name="creator_%(app_label)s_%(class)s_objects", 
                                limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
    updater = models.ForeignKey(User, blank=True, null=True, editable=False,
                                related_name="updater_%(app_label)s_%(class)s_objects",
                                limit_choices_to={'is_active': True}, on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True, editable=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        default_permissions = ()

    def save(self, *args, **kwargs):
        # Automatically set auto_id if it's not set
        if not self.auto_id:
            # Get the maximum value of auto_id in the current model and increment it
            last_instance = self.__class__.objects.order_by('-auto_id').first()
            if last_instance:
                self.auto_id = last_instance.auto_id + 1
            else:
                self.auto_id = 1  # Start from 1 if no instance exists

        # Call the parent save method to save the object
        super().save(*args, **kwargs)