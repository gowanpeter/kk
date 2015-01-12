from django.shortcuts import render, render_to_response, RequestContext
from gowan.forms import PieceForm, GlazeLookupForm, DocumentationForm, ConditionChoiceForm, ExhibitionForm

def home(request):

    form = PieceForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def GlazeView(request):

    form = GlazeLookupForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

def DocumentationView(request):

    form = DocumentationForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

def ConditionChoiceView(request):

    form = ConditionChoiceForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))


def ExhibitionView(request):

    form = ExhibitionForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()


    return render_to_response("kk.html",
                                locals(),
                                context_instance=RequestContext(request))

