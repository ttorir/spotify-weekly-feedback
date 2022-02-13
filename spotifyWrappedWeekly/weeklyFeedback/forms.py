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

class adminDashboardForm(forms.Form):
    playlist_csv_link = forms.CharField(label='playlist_csv', max_length=800)
    q1_option1 = forms.CharField(label='q1_option1', max_length=220)
    q1_option2 = forms.CharField(label='q1_option2', max_length=220)
    q2_option1 = forms.CharField(label='q2_option1', max_length=220)
    q2_option2 = forms.CharField(label='q2_option2', max_length=220)
    q3_option1 = forms.CharField(label='q3_option1', max_length=220)
    q3_option2 = forms.CharField(label='q3_option2', max_length=220)
