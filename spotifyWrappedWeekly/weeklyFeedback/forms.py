from django import forms

class SurveyForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    q1 = forms.IntegerField(label='value of the first slider')
    q2 = forms.IntegerField(label='value of the second slider')
    q3 = forms.IntegerField(label='value of the third slider')
    curr_track_id = forms.IntegerField(label='current_track_id')

class ButtonForm(forms.Form):
   curr_track_id = forms.IntegerField(label='current_track_id')
   username = forms.CharField(label='username', max_length=100)