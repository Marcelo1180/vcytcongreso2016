from django.shortcuts import render, RequestContext, HttpResponseRedirect
from forms import InvestigadorForm

# Create your views here.
def home(request):
    form = InvestigadorForm()
    if request.method == 'POST':
        form = InvestigadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # post = form.save(commit=False)
            # post.user = request.user
            # post.save()
            return HttpResponseRedirect('/add/publisher_thanks')
    return render(request, 'base.html', {'form': form}, context_instance=RequestContext(request))
    # return render(request, 'base.html')