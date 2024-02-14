from django.views.generic import TemplateView

class SnackListView(TemplateView):
    template_name='snack_list.html'
    
class SnackDetailView(TemplateView):
    template_name='snack_detail.html'
