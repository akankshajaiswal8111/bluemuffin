from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import CustomUser
from .models import Files
from .forms import CustomUserCreationForm
from .forms import DocumentForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#@login_required
#def files(request):

#@method_decorator(login_required, name='dispatch')
#class Upload(View):
#    form_class = UploadFileForm 
#    success_url = reverse_lazy('login')
#    template_name = 'upload.html'

#    def upload_file(request):
#        if request.method == 'POST':
#        uploaded_file = request.FILES['document']

#    return render(request,'upload.html')
#            form = UploadFileForm(request.POST, request.FILES)
 #       if form.is_valid():
 #           handle_uploaded_file(request.FILES['file'])
 #           return HttpResponseRedirect('/success/url/')
 #       else:
 #       form = UploadFileForm()
 #       return render(request, 'upload.html', {'form': form})

#@login_required
#def update(request, pk):

#@login_required
#def delete(request, pk):

#class UserFiles(View):
#    form_class = 
#    model = CustomUser
#    template_name = 'files_list.html'
def get(request):
    user = request.user
    files_list = user.files_set.all()
    return render(request, 'all_files.html', {'u_fname': user.first_name, 'u_lname': user.last_name, 'files' : files_list})
def post(request):
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        document = form.save(commit=False)
        document.user = request.user
        document.save()
        data = {'is_valid' : True, 'description': document.file.name, 'url' : document.file.url}
    else:
        data = {'is_valid' : False}
#    return JsonResponse(data)
    return render(request, 'model_form_upload.html', {'form' : form})

#class FilesUpdate(UpdateView):
#    model = Files
#    fields = ['file']
#    template_name_suffix = '_update_form'

def update(request, id):
    instance = get_object_or_404(Files, id=id)
    form = DocumentForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        newdoc = form.save(commit=False)
        newdoc.user = request.user
        newdoc.save()
    return render(request, 'model_form_upload.html', {'form': form})

def delete(request, id):
    doc = Files.objects.get(id=id)
    doc.delete()
    return render(request, 'list.html')

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #newdoc = Files(file = request.FILES['file'])
            newdoc = form.save(commit=False)
            newdoc.user = request.user
            newdoc.save()
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('users.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    user = request.user
    documents = user.files_set.all()
    # Render list page with the documents and the form
    return render(request, 'list.html', {'fname': user.first_name, 'lname': user.last_name, 'documents': documents, 'form': form} )


