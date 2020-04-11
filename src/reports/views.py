from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from django.contrib.auth.models import User
from .models import Report
from django.contrib.auth.decorators import login_required


class ReportListView(ListView):
    #################################################################################################
    # The logic here is handled in the view. all Users are passed in, but only those with
    # reports associated with their accounts are shown in the list. This was done this way to save time
    # A good deal of time was spent attempting to do this by only passing in a model containing Users
    # with a report to their name. This should be changed later to allow better efficiency with
    # a large number of users
    # This SO post was the inspiration for this solution
    # https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django
    #################################################################################################

    model = User

    # DEFAULT BEHAVIOR
    # looks for template with naming structure of <app>/<model>_<viewtype>.html
    # in this case it's looking for blogapp/post_list
    # DEFAULT BEHAVIOR
    # The naming here is slightly off of the default name structure.
    # I didn't look too deep into it, but this works.
    template_name = 'reports/reports_list.html'

    # by default, in the template Django is looking for something named {{ object_list }}.
    # The method for changing it is below if we wanted it to be called {{ users }}.
    # context_object_name = 'users'

    # I've put them in alphabetical order here. this is the order the object_list will
    # be given to the template. it can be sorted by any attribute of the model (User in this case)
    ordering = ['-last_name']

    # This allows for pagination. if you've gone through a tutorial, this should be self explanatory.
    # if not, check this: https://youtu.be/acOktTcTVEQ
    paginate_by = 15


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/report.html'
    context_object_name = 'report'

