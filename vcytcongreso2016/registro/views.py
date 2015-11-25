from django.shortcuts import render, RequestContext, HttpResponseRedirect
from forms import InvestigadorForm

# Create your views here.
def home(request):
    sw_error = "false"
    if request.method == 'POST':
        form = InvestigadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add/publisher_thanks')
        else:
            sw_error = "true"
    else:
        form = InvestigadorForm()
    return render(request, 'base.html', {'form': form, 'sw_error': sw_error}, context_instance=RequestContext(request))
    # return render(request, 'base.html')