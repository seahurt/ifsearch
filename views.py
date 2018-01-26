from django.shortcuts import render
from .models import If
from .iform import SearchForm
# Create your views here.


def search(request):
    if request.method == 'GET':
        journal = request.GET['journal']
        # journal = str(journal).lower()
        if journal == '':
            return render(request, 'ifsearch/index.html')
        year = str(request.GET['year'])
        year = ['2017','2016'] if year=='All' else [year]
        querys = If.objects.filter(journal__iexact=journal, year__in=year)
        # if something goes wrong, no info returned, do blur search
        if len(querys)==0:
            core_words = journal.split()
            core_string = [x for x in core_words if x != 'the' and x != 'of']
            querys = If.objects.filter(journal__icontains=' '.join(core_string),year__in=year).order_by('-iff')
            context = {
                'info': '{0} is not found, check the similar below'.format(journal.upper()),
                'ifs': querys,
                'journal': journal.upper(),}
            return render(request, 'ifsearch/result.html', context=context)
        # else: everything is OK, do below
        context = {
            'info': 'success',
            'ifs': querys,
            'journal': journal.upper(),}
        return render(request, 'ifsearch/result.html', context=context)

def index(request):
    return render(request, 'ifsearch/index.html')


