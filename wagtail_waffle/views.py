from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.viewsets.base import ViewSetGroup
from wagtail.admin.views.generic import IndexView
from wagtail.admin.ui.tables import (
    BulkActionsCheckboxColumn,
    InlineActionsTable,
)
from waffle.models import Flag, Sample, Switch


class IndexView(IndexView):
    table_class = InlineActionsTable
    template_name = "waffle/index.html"

    def get_columns(self):
        return [
            BulkActionsCheckboxColumn("checkbox", accessor=lambda obj: obj),
            *super().get_columns(),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update(
            {
                "model_opts": self.model._meta,
            }
        )

        return context
    
class BaseAdmin(ModelViewSet):
    search_fields = ('name', 'note')
    exclude_form_fields = ["created", "modified"]
    index_view_class = IndexView


class FlagAdmin(BaseAdmin):
    model = Flag
    list_display = ('name', 'note', 'everyone', 'percent', 'superusers',
                    'staff', 'authenticated', 'languages')
    list_filter = ('everyone', 'superusers', 'staff', 'authenticated')
    ordering = ('-id',)

class SampleAdmin(BaseAdmin):
    model = Sample
    list_display = ('name', 'percent', 'note', 'created', 'modified')
    ordering = ('-id',)

class SwitchAdmin(BaseAdmin):
    model = Switch
    list_display = ('name', 'active', 'note', 'created', 'modified')
    list_filter = ('active',)
    ordering = ('-id',)

class WaffleViewSetGroup(ViewSetGroup):
    menu_label = "Features"
    menu_icon = "pick"
    add_to_admin_menu = True
    items = (SwitchAdmin(), FlagAdmin(), SampleAdmin())