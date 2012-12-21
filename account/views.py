# coding: utf-8
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _



def view_profile(request):
    if request.user:
        try:
            profile = request.user.get_profile()
        except ObjectDoesNotExist:
            raise Http404(_('Profile does not exist'))
        return render_to_response(
            'account/index.html',
            {
                'user': request.user,
                'profile': request.user.get_profile()
            },
            context_instance=RequestContext(request),
        )
    else:
        return HttpResponse(_('Login Required'), status=403)
