from django.shortcuts import render
from django.http import HttpResponseRedirect
#这条漏了orz
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))