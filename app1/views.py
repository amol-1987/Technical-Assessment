from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from app1.forms import NewUserForm
from app1.models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'users.html',{'form':form})



class UserList(ListView):
	model = User
	context_object_name = 'users'
	template_name = 'search.html'

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['users']=context['users']

		search_input = self.request.GET.get('search-area') or ''
		if search_input:
			context['users']=context['users'].filter(name__icontains=search_input)
			
		context['search_input']=search_input
		return context




class UserDetail(DetailView):
	model = User
	context_object_name = 'user'
	template_name = 'detail.html'


def images(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'images.html',{'form':form})
