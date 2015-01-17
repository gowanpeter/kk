from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from gowan.forms importGlazeLookupForm


def dimensionsView(request):

    form = dimensionForm(request.POST or None)

    if form.is_valid():
        save_it = fhoorm.save(commit=False)
        save_it.save()

    return render_to_response("kk.html",
                              locals(),
                              context_instance=RequestContext(request))


class PieceForm(forms.ModelForm):

        class Meta:
            model = Piece
            fields = "__all__"
