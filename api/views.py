from django.shortcuts import render
from meetings.models import Meeting, MeetingSubType
from online.models import OnlineMeeting
from rest_framework import viewsets, generics, views
from api.serializers import (
    MeetingSearchSerializer,
    OnlineMeetingSerializer,
    MeetingGuideSerializer,
)
from datetime import datetime, timedelta
from django.db.models import Q
from django.db.models import IntegerField, Value
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters
from django.db.models import Avg, F, Window
from django.db.models.functions import Rank
from django.utils import timezone
import pytz
from django.contrib.postgres.search import SearchVector

# Create your views here.


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all().order_by("time")
    serializer_class = MeetingSearchSerializer


class MeetingsList(generics.ListAPIView):
    """
    Return a list of all the products that the authenticated
    user has ever purchased, with optional filtering.
    """

    model = Meeting
    serializer_class = MeetingSearchSerializer

    def get_queryset(self):
        twentyfour = self.request.query_params.get("twentyfour", None)
        if twentyfour == "1":
            tz = pytz.timezone("Europe/London")
            now = datetime.datetime.now(tz=tz)

            now = datetime.now()
            date_today = now.date()
            time_now = now.time()
            datetime_now = datetime.combine(date_today, time_now)
            day_name_today = now.strftime("%A")
            tomorrow = now + timedelta(days=1)
            day_name_tomorrow = tomorrow.strftime("%A")

            meetings_today = Meeting.objects.filter(
                (Q(day=day_name_today) & Q(time__gte=now.time()))
            )
            meetings_tomorrow = Meeting.objects.filter(
                (Q(day=day_name_tomorrow) & Q(time__lte=now.time()))
            )
            rank_by_day = Window(
                expression=Rank(), partition_by=F("day"), order_by=F("time").asc()
            )

            all = meetings_today | meetings_tomorrow
            if day_name_today == "sunday":
                all_ordered = all.order_by("-day_number", "time")
            else:
                all_ordered = all.order_by("day_number", "time")
            return all_ordered

        return Meeting.objects.all()


class MeetingAutofillSearch(generics.ListAPIView):
    model = Meeting
    serializer_class = MeetingSearchSerializer

    def get_queryset(self):

        title = self.request.query_params.get("title", "").lower()
        type = self.request.query_params.get("type", "")
        return (
            Meeting.objects.filter(type=type)
            .filter(published=True)
            .filter(title__iexact=title)
            .order_by("-created")
        )


class MeetingSearch(generics.ListAPIView):

    model = Meeting
    serializer_class = MeetingSearchSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["time_band"]
    ordering_fields = ["day_number", "time"]

    def get_queryset(self):

        queryset = Meeting.objects.filter(published=True).annotate(
            search=SearchVector("postcode", "title","postcode"),
        )
        year = datetime.now().date().year
        month = datetime.now().date().month
        today = datetime.now()

        search = self.request.query_params.get("search", None)

        if search is not None and len(search) > 0:
            queryset = queryset.filter(search=search)

        day = self.request.query_params.get("day", None)
        if day:
            if day == "now":
                now = datetime.now()
                time_now = now.time()
                day_name_today = now.strftime("%A")
                queryset = queryset.filter(
                    ((Q(days__value=day_name_today)) & Q(time__gte=time_now))
                )
            else:
                queryset = queryset.filter(days__value=day)

        meeting_type = self.request.query_params.get("type", None)
        if meeting_type and meeting_type != 'undefined':
            queryset = queryset.filter(((Q(type=meeting_type)) | Q(type="HYB")))

        wheelchair = self.request.query_params.get("wheelchair", None)
        if wheelchair:
            queryset = queryset.filter(sub_types__value="Wheelchair Access")

        return queryset.order_by("day_number", "time")


class OnlineMeetingSearch(generics.ListAPIView):
    """
    Return a list of all the products that the authenticated
    user has ever purchased, with optional filtering.
    """

    model = Meeting
    serializer_class = OnlineMeetingSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        "time_band",
    ]
    ordering_fields = ["time"]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        day = self.request.query_params.get("day", None)
        tz = pytz.timezone("Europe/London")
        dt_now = datetime.now(tz=tz) - timedelta(minutes=10)
        day_name_today = dt_now.strftime("%A")
        queryset = Meeting.objects.annotate(
            search=SearchVector("description", "title"),
        )
        queryset = queryset.filter(published=True)
        year = datetime.now().date().year
        month = datetime.now().date().month
        today = datetime.now()

        search = self.request.query_params.get("search", None)

        if search is not None and len(search) > 0:
            queryset = queryset.filter(search=search)

        now = self.request.query_params.get("now", None)
        top = int(self.request.query_params.get("top", 0))

        if day == "now" or now == "1":

            date_today = dt_now.date()
            time_now = dt_now.time()

            tomorrow = dt_now + timedelta(days=1)

            meetings_today = Meeting.objects.filter(
                ((Q(days__value=day_name_today)) & Q(time__gte=dt_now.time()))
            ).filter(published=True)

            all = meetings_today  # | meetings_tomorrow
            if day_name_today == "sunday":
                all_ordered = all.order_by("time")
            else:
                all_ordered = all.order_by("time")

            if top:
                all_ordered = all_ordered[:top]
            return all_ordered  # .annotate(the_rank=rank_by_day)
        elif day in [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]:
            queryset = queryset.filter(Q(days__value=day))

        return queryset.order_by("time")


class MeetingGuideListView(generics.ListAPIView):
    """
    Return a list of meetings for the meetingguide app.
    """

    model = Meeting
    serializer_class = MeetingGuideSerializer
    queryset = Meeting.objects.filter(published=True)
    pagination_class = None


class MeetingGuideViewSet(viewsets.ModelViewSet):
    """
    Provide a ViewSet for Django Default Router so that MeetingGuide endpoint
    can be accessed with `.json` suffix.
    """

    queryset = Meeting.objects.filter(published=True)
    serializer_class = MeetingGuideSerializer
    pagination_class = None
