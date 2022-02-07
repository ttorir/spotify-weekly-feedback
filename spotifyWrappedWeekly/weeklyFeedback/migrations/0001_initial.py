# Generated by Django 4.0.2 on 2022-02-06 00:05

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NameSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arbitrary_id', models.IntegerField(blank=True, null=True, verbose_name='unique_id_for_a_song')),
                ('text_entry', models.CharField(max_length=200, verbose_name='week_song_was_added')),
            ],
            options={
                'verbose_name': 'Sample Model',
                'verbose_name_plural': 'Sample Models',
            },
        ),
        migrations.CreateModel(
            name='PlaylistSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.IntegerField(blank=True, null=True, verbose_name='unique_id_for_a_song')),
                ('week_added', models.CharField(max_length=200, verbose_name='week_song_was_added')),
                ('track_name', models.CharField(max_length=200, verbose_name='track_name')),
                ('track_artists', models.CharField(max_length=200, verbose_name='track_artists')),
                ('artist_genres', models.CharField(max_length=200, verbose_name='artist_genres')),
                ('artist_popularity', models.CharField(max_length=200, verbose_name='artist_popularity')),
                ('track_album', models.CharField(max_length=200, verbose_name='track_album')),
                ('track_duration', models.IntegerField(blank=True, null=True, verbose_name='track_duration')),
                ('album_release_yyyy', models.IntegerField(blank=True, null=True, verbose_name='year_of_release_YYYY')),
                ('album_release_mm', models.IntegerField(blank=True, null=True, verbose_name='year_of_release_MM')),
                ('album_release_dd', models.IntegerField(blank=True, null=True, verbose_name='year_of_release_DD')),
                ('artist_image', models.CharField(max_length=5000, verbose_name='artist_image')),
                ('track_image', models.CharField(max_length=5000, verbose_name='track_image')),
                ('added_by', models.CharField(max_length=200, verbose_name='added_by')),
                ('added_at', models.CharField(max_length=200, verbose_name='date_added')),
            ],
            options={
                'verbose_name': 'PlaylistSong',
                'verbose_name_plural': 'PlaylistSongs',
            },
        ),
        migrations.CreateModel(
            name='SongReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(blank=True, null=True, verbose_name='unique_id_for_a_review')),
                ('track_id', models.IntegerField(blank=True, null=True, verbose_name='unique_id_for_a_song')),
                ('review_response', jsonfield.fields.JSONField(blank=True, dump_kwargs={'ensure_ascii': False}, null=True, verbose_name='review_response')),
                ('reviewed_at', models.CharField(max_length=200, verbose_name='date_reviewed')),
            ],
            options={
                'verbose_name': 'SongReview',
                'verbose_name_plural': 'SongReview',
            },
        ),
    ]
