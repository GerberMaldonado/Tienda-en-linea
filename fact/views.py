import io
from django.views.generic import TemplateView, CreateView
from .forms import ClientForm
from django.shortcuts import redirect ,render
from django.urls import reverse_lazy

# Create your views here.
class FactView(TemplateView):
	template_name='fact/index_create_form.html'

class CrearClient(CreateView):	
	template_name= 'fact/index_create_form.html'
	form_class = ClientForm
	success_url = reverse_lazy('orders:process_order')

def Create_Client(request):

	if request.method == 'GET':
		return render(request, 'fact/index_create_form.html')

	if request.method == 'POST':
		form = ClientForm(request.POST)

		if form.is_valid():
			form.save()

			return redirect ('process_order')

