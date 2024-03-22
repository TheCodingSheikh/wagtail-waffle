from django.contrib.auth.models import Permission
from wagtail import hooks

from .views import WaffleViewSetGroup
from .bulk_actions import (
    EnableForAllBulkAction,
    DisableForAllBulkAction,
    EnableSwitchesBulkAction,
    DisableSwitchesBulkAction,
    DeleteFlagBulkAction,
    DeleteSwitchBulkAction,
    DeleteSampleBulkAction
)

@hooks.register("register_admin_viewset")
def register_viewset():
    return WaffleViewSetGroup()

@hooks.register("register_permissions")
def permissions_hook():
    return Permission.objects.filter(
        content_type__app_label="waffle",
            )

for action_class in [EnableForAllBulkAction, DisableForAllBulkAction, EnableSwitchesBulkAction, DisableSwitchesBulkAction, DeleteFlagBulkAction, DeleteSwitchBulkAction, DeleteSampleBulkAction]:
    hooks.register("register_bulk_action", action_class)