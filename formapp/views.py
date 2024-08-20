from django.views.generic import TemplateView
#from forms import Register
#from django.contrib import r
from .forms import MasterClassRegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.


 #
#from .forms import SeminarRegistrationForm
#from .models import SeminarRegistration

#def register_seminar(request):
#if request.method == 'POST':
      #  form = SeminarRegistrationForm(request.POST)
       # if form.is_valid():
        #    registration = SeminarRegistration(
#name=form.cleaned_data['name'],
#email=form.cleaned_data['email'],
#phone=form.cleaned_data['phone'],
         #       topic=form.cleaned_data['topic']
         #   )
         #   registration.save()
            # Redirect to a success page or display a success message
    #else:
   #     form = SeminarRegistrationForm()

   # return render(request, 'seminar_registration.html', {'form': form})#
class HomepageView(TemplateView):
    template_name = "register.html"

class SignUpView(CreateView):
        form_class = MasterClassRegistrationForm
        success_url = reverse_lazy('success')
        template_name = 'register.html'
        context_object_name = "form"


class SuccessView(TemplateView):
    template_name = 'success.html'