from distutils.debug import DEBUG
from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from django.conf import settings
from .forms import *
from .models import *
from datetime import datetime, timedelta
import pandas as pd
import json
import os
from os import listdir
from os.path import isfile, join
import ast

#def index(request):

def format_artist_list(artist_list):
    row_entry = ast.literal_eval(artist_list)
    if len(row_entry) > 1:
        row_entry = ", ".join(row_entry)
    else:
        row_entry = row_entry[0]
    return row_entry

def format_artists(playlist):
    reformatting = []
    for idx, row in playlist.iterrows():
        reformatting.append(format_artist_list(row['track_artists']))
    playlist['scream'] = reformatting
    return playlist

class weeklySummaryView(View):
    def get(self, request, *args, **kwargs):
        all_song_objects = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).all()
        formatted_df = pd.DataFrame(columns=['track_image','track_title','formatted_artist','q1','q2','q3'])
        for song in all_song_objects:
            access_user_review =  SongReview.objects.filter(track_id=song.track_id)
            if access_user_review.count():
                access_user_review = access_user_review.all()
                for review in access_user_review:
                    formatted_df.loc[len(formatted_df)] = [song.track_image,song.track_name, format_artist_list(song.track_artists), review.q1,review.q2,review.q3]
        song_stats_df = pd.DataFrame(columns = ['track_image','track_title','formatted_artist','q1','q2','q3'])
        for song, song_df in formatted_df.groupby('track_title'):
            song_stats_df.loc[len(song_stats_df)] = [song_df['track_image'].iloc[0], song, song_df['formatted_artist'].iloc[0],song_df['q1'].mean(),song_df['q2'].mean(),song_df['q3'].mean()]
        ranking_df = pd.DataFrame(columns=['option_1','option_2','list_of_images'])
        
        def return_options_for_qs(question_number):
            question_object = WeeklySliders.objects.filter(form_field=question_number,week_id=1).first()
            return [question_object.option_1, question_object.option_2]
        q1_opts = return_options_for_qs('q1')
        q2_opts = return_options_for_qs('q2')
        q3_opts = return_options_for_qs('q3')
        ranking_df.loc[len(ranking_df)] = [q1_opts[0],q1_opts[1],list(song_stats_df.sort_values('q1')['track_image'])]    
        ranking_df.loc[len(ranking_df)] = [q2_opts[0],q2_opts[1],list(song_stats_df.sort_values('q2')['track_image'])]   
        ranking_df.loc[len(ranking_df)] = [q3_opts[0],q3_opts[1],list(song_stats_df.sort_values('q3')['track_image'])]     
        context = {
            'sorted_images':ranking_df,
        }
        if 'username' in request.session:
            context['username'] = request.session['username']
        return render(request, "weeklySummary.html",context)

class userSummaryView(View):
    def get(self, request, *args, **kwargs):
        username = request.session['username']
        all_song_objects = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).all()
        formatted_df = pd.DataFrame(columns=['track_image','track_title','formatted_artist','q1','q2','q3'])
        for song in all_song_objects:
            access_user_review =  SongReview.objects.filter(username = username,track_id=song.track_id)
            if access_user_review.count():
                access_user_review = access_user_review.last()
                formatted_df.loc[len(formatted_df)] = [song.track_image,song.track_name, format_artist_list(song.track_artists), access_user_review.q1,access_user_review.q2,access_user_review.q3]
        q1 = WeeklySliders.objects.filter(form_field='q1',week_id=1).first()
        q2 = WeeklySliders.objects.filter(form_field='q2',week_id=1).first()
        q3 = WeeklySliders.objects.filter(form_field='q3',week_id=1).first()
        context = {
            'username':username,
            'formatted_df':formatted_df,
            'q1':q1,
            'q2':q2,
            'q3':q3,
        }
        if 'username' in request.session:
            context['username'] = request.session['username']
        return render(request, "userSummary.html",context)

class landingPageView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if 'username' in request.session:
            context['username'] = request.session['username']
        return render(request, "landing.html",context)
    def post(self, request, *args, **kwargs):
        form = SurveyForm(request.POST)
        request.session['username'] = form['username'].value()
        return redirect('feedback_page')#render(request, "songFocus.html", context)

class weeklyFeedbackView(View):
    
    def get(self, request, *args, **kwargs):
        this_song = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).first()
        curr_playlist = format_artists(active_playlist)
        number_of_entries = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).count() - this_song.track_id
        context = {
            'this_song':this_song,
            'formatted_artists':format_artist_list(this_song.track_artists),
            'weekly_slider_qs':WeeklySliders.objects.filter(week_id=1).all(),
            'song_count':'1 / '+str(number_of_entries),
        }
        if 'username' in request.session:
            context['username'] = request.session['username']
            if SongReview.objects.filter(username = request.session['username'],track_id=0).exists():
                context['previous_answer'] = SongReview.objects.filter(username = request.session['username'],track_id=0).last()
                
        return render(request, "songFocus.html", context)

    def post(self, request, *args, **kwargs):
        # create a form instance and populate it with data from the request:
        weekly_slider_qs = WeeklySliders.objects.filter(week_id=1).all()
        curr_playlist = format_artists(active_playlist)
        highest_task_id = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).count() - 1
        first_song_id = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).first()
        number_of_entries = PlaylistSongs.objects.filter(added_at__gte=(datetime.now()-timedelta(days = 7))).count() - first_song_id.track_id
        if request.POST.get("prev"):
            form = ButtonForm(request.POST)
            curr_track_id = int(form['curr_track_id'].value())
            
            if curr_track_id > first_song_id.track_id:
                next_song_num = int(curr_track_id)-1
            else:
                next_song_num = highest_task_id
            next_song = PlaylistSongs.objects.get(track_id=next_song_num)
            context = {
                'this_song':next_song,
                'formatted_artists':format_artist_list(next_song.track_artists),
                'username':request.POST.get("username"),
                'weekly_slider_qs':weekly_slider_qs,
                'song_count':str(int(next_song_num)+1-first_song_id.track_id)+' / '+str(number_of_entries),
            }
            if SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num).exists():
                context['previous_answer'] = SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num).last()
                  
            return render(request, "songFocus.html", context) 
        elif request.POST.get("next"):
            form = ButtonForm(request.POST)
            curr_track_id = int(form['curr_track_id'].value())
            if curr_track_id < highest_task_id:
                next_song_num = int(curr_track_id)+1
            else:
                next_song_num = 0
            next_song = PlaylistSongs.objects.get(track_id=next_song_num)
            context = {
                'this_song':next_song,
                'formatted_artists':format_artist_list(next_song.track_artists),
                'username':request.POST.get("username"),
                'weekly_slider_qs':weekly_slider_qs,
                'song_count':str(int(next_song_num)+1-first_song_id.track_id)+' / '+str(number_of_entries),
            }
            if SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num).exists():
                context['previous_answer'] = SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num).last()
                
            return render(request, "songFocus.html", context) 
        elif (SurveyForm(request.POST)):
            form = SurveyForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                curr_track_id = int(form['curr_track_id'].value())
                num_forms = SongReview.objects.count()
                if SongReview.objects.filter(track_id=curr_track_id, username=form['username'].value(),reviewed_at__gte=(datetime.now()-timedelta(days = 7))).exists():
                    this_song_review = SongReview.objects.filter(track_id=curr_track_id, username=form['username'].value()).last()
                    this_song_review.q1 =form['q1'].value()
                    this_song_review.q2 =form['q2'].value()
                    this_song_review.q3 =form['q3'].value()
                    this_song_review.reviewed_at = datetime.now()
                else:
                    this_song_review = SongReview(track_id=curr_track_id, username=form['username'].value(), q1=form['q1'].value(),q2=form['q2'].value(),q3=form['q3'].value(),reviewed_at = datetime.now())
                this_song_review.save()
                if curr_track_id < highest_task_id:
                    next_song_num = int(curr_track_id)+1
                else:
                    next_song_num = 0
                next_song = PlaylistSongs.objects.get(track_id=next_song_num)
                context = {
                    'this_song':next_song,
                    'formatted_artists':format_artist_list(next_song.track_artists),
                    'username':request.POST.get("username"),
                    'weekly_slider_qs':weekly_slider_qs,
                    'song_count':str(int(next_song_num)+1-first_song_id.track_id)+' / '+str(number_of_entries),
                }
                if SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num).exists():
                    context['previous_answer'] = SongReview.objects.filter(username = form['username'].value(),track_id=next_song_num,reviewed_at__gte=(datetime.now()-timedelta(days = 7))).last()
                
                return render(request, "songFocus.html", context) 
        else:  
            print('no name form')  

        return render(request, "songFocus.html")

active_playlist = pd.read_csv('https://raw.githubusercontent.com/ttorir/spotify-wrapped-weekly-public/main/active_week01.csv')
#active_playlist = pd.read_csv('https://raw.githubusercontent.com/ttorir/spotify-wrapped-weekly-public/main/active.csv')
num_skipped = 0
for idx, row in active_playlist.iterrows():
    if PlaylistSongs.objects.filter(track_name=row['track_name'],added_at__gte=(datetime.now()-timedelta(days = 7))):
        num_skipped +=1
    else:
        if type(row['album_release:mm']) == int:
            month = row['album_release:mm']
            day = row['album_release:dd']
        else:
            month = 0
            day = 0
        p = PlaylistSongs(track_id=PlaylistSongs.objects.count(),
                        track_name=row['track_name'],
                        track_artists=row['track_artists'],
                        artist_genres=row['artist_genres'],
                        artist_popularity=row['artist_popularity'],
                        track_album=row['track_album'],
                        track_duration=row['track_duration'],
                        album_release_yyyy=row['album_release:yyyy'],
                        album_release_mm = month,
                        album_release_dd = day,
                        artist_image=row['artist_image'],
                        track_image=row['track_image'],
                        added_by=row['added_by'],
                        added_at=row['added_at'],
                        track_spotify_address=row['track_id'],
                        track_src=row['embed_src'],
                        )
        p.save()

questions_list_1 = [['q1','cheesecake factory bathroom','dennys parking lot'],['q2','me','my evil british twin'],['q3','windows down bop','carpool karaoke']]
for question in questions_list_1:
    does_this_exist = WeeklySliders.objects.filter(form_field = question[0],week_id=1).exists()
    if not does_this_exist:
        b = WeeklySliders(week_id = 1, form_field = question[0], option_1 = question[1], option_2= question[2], added_on=str(datetime.now()))
        b = b.save()
    else:
        b = WeeklySliders.objects.filter(form_field = question[0]).last()
        b.week_id = 1
        b.save()
"""
"""