# coding: utf-8
""" Account views """
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from account.models import Account
from account.forms import AccountEditForm


@login_required(login_url='/login/')
def view_profile(request):
    try:
        profile = request.user.get_profile()
    except ObjectDoesNotExist:
        raise Http404(_('Profile does not exist'))
    return render_to_response(
        'account/index.html',
        {
            'user': request.user,
            'profile': profile
        },
        context_instance=RequestContext(request),
    )


@login_required(login_url='/login/')
def edit_profile(request):
    try:
        profile = request.user.get_profile()
    except ObjectDoesNotExist:
        profile = Account.objects.create(user=request.user)
    if request.method == 'POST':
        form = AccountEditForm(
            request.POST,
            instance=profile,
        )
        if form.is_valid():
            form.save()
    else:
        form = AccountEditForm(instance=profile)

    return render_to_response(
        'account/edit.html',
        {
            'user': request.user,
            'profile': profile,
            'form': form,
        },
        context_instance=RequestContext(request),
    )
