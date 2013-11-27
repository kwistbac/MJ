from django.shortcuts import render_to_response, render
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from mJuke.models import Song


def playlist(request):
    try:
        songs = Song.objects.all().filter(account=request.user).exclude(queue=0).order_by('-queue')[:15]
        curSong = Song.objects.all().get(queue=0, account=request.user)
        return render_to_response("establishment/playlist/playlist.html", {'songs': songs, 'curSong': curSong},
                                  context_instance=RequestContext(request))
    except Song.DoesNotExist:
        return HttpResponse('Songs were not found for this user.')