from django.utils.translation import gettext_lazy as _
from django.utils.functional import classproperty
from wagtail.admin.views.bulk_action import BulkAction
from wagtail.snippets.permissions import get_permission_name
from wagtail.admin.admin_url_finder import AdminURLFinder
from waffle.models import Flag, Sample, Switch

class WaffleBulkAction(BulkAction):
    template_name = "waffle/action.html"
    
    def check_perm(self, obj):
        self.can_change_items = self.request.user.has_perm(
            get_permission_name("change", self.model)
        )
        return self.can_change_items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "waffle_type": (
                    self.model._meta
                ),
                "action": (
                    self.action_type
                ),
            }
        )
        return context
    

class EnableForAllBulkAction(WaffleBulkAction):
    models = [Flag]
    aria_label = _("Enable selected flags for everyone")
    display_name = _("Enable for all")
    action_type = "enable"
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).update(everyone=True)
        return len(objects), 0


class DisableForAllBulkAction(WaffleBulkAction):
    models = [Flag]
    aria_label = _("Disable selected flags for everyone")
    display_name = _("Disable for all")
    action_type = "disable"
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).update(everyone=False)
        return len(objects), 0
    

class EnableSwitchesBulkAction(WaffleBulkAction):
    models = [Switch]
    aria_label = _("Enable selected switches")
    display_name = _("Enable for all")
    action_type = "enable"
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).update(active=True)
        return len(objects), 0


class DisableSwitchesBulkAction(WaffleBulkAction):
    models = [Switch]
    aria_label = _("Disable selected switches")
    display_name = _("Disable for all")
    action_type = "disable"
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).update(active=False)
        return len(objects), 0
    

class DeleteWaffleBulkAction(WaffleBulkAction):
    aria_label = _("Delete selected")
    action_type = "delete"
    display_name = _("Delete")
    classes = {"serious"}

    def check_perm(self, object):
        self.can_delete_items = self.request.user.has_perm(
            get_permission_name("delete", self.model)
        )
        return self.can_delete_items
    
    @classmethod
    def execute_action(cls, objects, **kwargs):
        cls.get_default_model().objects.filter(
            pk__in=[obj.pk for obj in objects]
        ).delete()
        return len(objects), 0


class DeleteFlagBulkAction(DeleteWaffleBulkAction):
    models = [Flag]


class DeleteSwitchBulkAction(DeleteWaffleBulkAction):
    models = [Switch]

    
class DeleteSampleBulkAction(DeleteWaffleBulkAction):
    models = [Sample]
