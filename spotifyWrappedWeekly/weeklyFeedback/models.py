from __future__ import division, unicode_literals
from django.db import models

# -*- coding: utf-8 -*-

from typing import cast

from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import (
        gettext_lazy as _, pgettext_lazy)
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

from typing import List, Dict, Any, Optional, Text, Iterable, Tuple, FrozenSet, TYPE_CHECKING  # noqa

from jsonfield import JSONField

# Create your models here.
class WeeklySliders(models.Model):
        week_id = models.IntegerField(blank=True, null=True,
                verbose_name=_("week_question"))
        form_field = models.CharField(max_length=200,
                verbose_name=_("algins_this_to_a_form"))
        option_1 = models.CharField(max_length=200,
                verbose_name=_("option_1"))
        option_2 = models.CharField(max_length=200,
                verbose_name=_("option_2"))
        added_on = models.CharField(max_length=200,
                verbose_name=_("date_added"))
        class Meta:
                managed = True
                verbose_name = _("Slider Question")
                verbose_name_plural = _("Slider Questions")

        def __unicode__(self):
                return _(self.option_1 + ' or ' + self.option_2)

        __str__ = __unicode__


class WeeklySlidersSuggestion(models.Model):
        option_1 = models.CharField(max_length=200,
                verbose_name=_("option_1"))
        option_2 = models.CharField(max_length=200,
                verbose_name=_("option_2"))
        added_on = models.CharField(max_length=200,
                verbose_name=_("date_added"))
        class Meta:
                managed = True
                verbose_name = _("Suggested Slider Question")
                verbose_name_plural = _("Suggested Slider Questions")

        def __unicode__(self):
                return _('suggestion: ' + self.option_1 + ' or ' + self.option_2)

        __str__ = __unicode__

class NameSample(models.Model):
        arbitrary_id = models.IntegerField(blank=True, null=True,
                verbose_name=_("unique_id_for_a_song"))
        text_entry = models.CharField(max_length=200,
                verbose_name=_("week_song_was_added"))
        q1 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        q2 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        q3 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        class Meta:
                managed = True
                verbose_name = _("Sample Model")
                verbose_name_plural = _("Sample Models")

        def __unicode__(self):
                return self.arbitrary_id

        __str__ = __unicode__

class PlaylistSongs(models.Model):
        """
        Model for each song added to the playlists
        """
        track_id = models.IntegerField(blank=True, null=True,
                verbose_name=_("unique_id_for_a_song"))
        track_name = models.CharField(max_length=1000,
                verbose_name=_("track_name"))
        track_artists = models.CharField(max_length=2500,
                verbose_name=_("track_artists"))
        artist_genres = models.CharField(max_length=2000,
                verbose_name=_("artist_genres"))
        artist_popularity = models.CharField(max_length=200,
                verbose_name=_("artist_popularity"))
        track_album = models.CharField(max_length=1000,
                verbose_name=_("track_album"))
        track_duration = models.IntegerField(blank=True, null=True,
                verbose_name=_("track_duration"))
        album_release_yyyy = models.IntegerField(blank=True, null=True,
                verbose_name=_("year_of_release_YYYY"))
        album_release_mm = models.IntegerField(blank=True, null=True,
                verbose_name=_("year_of_release_MM"))
        album_release_dd = models.IntegerField(blank=True, null=True,
                verbose_name=_("year_of_release_DD"))
        artist_image = models.CharField(max_length=5500,
                verbose_name=_("artist_image"))
        track_image = models.CharField(max_length=5000,
                verbose_name=_("track_image"))
        added_by = models.CharField(max_length=200,
                verbose_name=_("added_by"))
        track_spotify_address = models.CharField(max_length=1000,
                verbose_name=_("track_spotify_id"))
        track_src = models.CharField(max_length=1000,
                verbose_name=_("track_src"))
        added_at = models.CharField(max_length=200,
                verbose_name=_("date_added"))
        

        class Meta:
                managed = True
                verbose_name = _("PlaylistSong")
                verbose_name_plural = _("PlaylistSongs")

        def __unicode__(self):
                return str(self.track_id)

        __str__ = __unicode__

class SongReview(models.Model):
        """
        Review for the Song
        """
        track_id = models.IntegerField(blank=True, null=True,
                verbose_name=_("unique_id_for_a_song"))
        username = models.CharField(max_length=200,
                verbose_name=_("username_of_who_added"))
        q1 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        q2 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        q3 = models.IntegerField(blank=True, null=True,
                verbose_name=_("slider value"))
        reviewed_at = models.CharField(max_length=200,
                verbose_name=_("date_reviewed"))
        
        class Meta:
                managed = True
                verbose_name = _("SongReview")
                verbose_name_plural = _("SongReview")

        def __unicode__(self):
                return {
                        "review_id": self.review_id,
                        "track_id": self.track_id,
                        }

        __str__ = __unicode__
