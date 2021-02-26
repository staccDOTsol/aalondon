# Generated by Django 2.2.18 on 2021-02-14 10:59

from django.db import migrations
from django.utils.text import slugify

INTERGROUPS = [
    "City Of London",
    "East London",
    "Chelsea",
    "Chelsea & Fulham",
    "London North East",
    "London North",
    "London North Middlesex",
    "London North West",
    "London South Middlesex",
    "London West End",
    "London Westway",
    "London Croydon Epsom & Sutton",
    "London North Kent",
    "London South East (East)",
    "London South East (West)",
    "London South",
    "London South West",
]

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

MEETING_SUB_TYPES = [
    ("11", "11th Step Meditation"),
    ("12x12", "12 Steps & 12 Traditions"),
    ("ASL", "American Sign Language"),
    ("ABSI", "As Bill Sees It"),
    ("BA", "Babysitting Available"),
    ("B", "Big Book"),
    ("H", "Birthday"),
    ("BRK", "Breakfast"),
    ("CAN", "Candlelight"),
    ("CF", "Child-Friendly"),
    ("C", "Closed"),
    ("AL-AN", "Concurrent with Al-Anon"),
    ("AL", "Concurrent with Alateen"),
    ("XT", "Cross Talk Permitted"),
    ("DR", "Daily Reflections"),
    ("DB", "Digital Basket"),
    ("D", "Discussion"),
    ("DD", "Dual Diagnosis"),
    ("EN", "English"),
    ("FF", "Fragrance Free"),
    ("FR", "French"),
    ("G", "Gay"),
    ("GR", "Grapevine"),
    ("HE", "Hebrew"),
    ("NDG", "Indigenous"),
    ("ITA", "Italian"),
    ("JA", "Japanese"),
    ("KOR", "Korean"),
    ("L", "Lesbian"),
    ("LIT", "Literature"),
    ("LS", "Living Sober"),
    ("LGBTQ", "LGBTQ"),
    ("TC", "Location Temporarily Closed"),
    ("MED", "Meditation"),
    ("M", "Men"),
    ("N", "Native American"),
    ("BE", "Newcomer"),
    ("NS", "Non-Smoking (ignored by Meeting Guide importer)"),
    ("ONL", "Online (ignored by Meeting Guide importer)"),
    ("O", "Open"),
    ("OUT", "Outdoor"),
    ("POC", "People of Color"),
    ("POL", "Polish"),
    ("POR", "Portuguese"),
    ("P", "Professionals"),
    ("PUN", "Punjabi"),
    ("RUS", "Russian"),
    ("A", "Secular"),
    ("SEN", "Seniors"),
    ("SM", "Smoking Permitted"),
    ("S", "Spanish"),
    ("SP", "Speaker"),
    ("ST", "Step Study"),
    ("TR", "Tradition Study"),
    ("T", "Transgender"),
    ("X", "Wheelchair Access"),
    ("XB", "Wheelchair-Accessible Bathroom"),
    ("W", "Women"),
    ("Y", "Young People"),
    ("SIG", "British Sign Language"),
    ("CHI", "Chits"),
    ("CRE","Creche")

]


def create_meeting_references(apps, schema_editor):
    # We can't import the Relections model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    MeetingDay = apps.get_model("meetings", "MeetingDay")
    MeetingIntergroup = apps.get_model("meetings", "MeetingIntergroup")
    MeetingSubType = apps.get_model("meetings", "MeetingSubType")

    intergroups = []
    for day in DAYS:
        _, _ = MeetingDay.objects.update_or_create(value=day)

    for intergroup in INTERGROUPS:
        _, _ = MeetingIntergroup.objects.update_or_create(value=intergroup)

    for sub_type in MEETING_SUB_TYPES:
        _, _ = MeetingSubType.objects.update_or_create(
            code=sub_type[0], value=sub_type[1]
        )


def migrate_physical_meeting_data(apps, schema_editor):

    """
    types->subtypes
    detail->description
    day->days
    
    """
    Meeting = apps.get_model("meetings", "Meeting")
    MeetingSubType = apps.get_model("meetings", "MeetingSubType")
    MeetingDay = apps.get_model("meetings", "MeetingDay")
    meetings = Meeting.objects.all()

    for meeting in meetings:
        meeting_types = (
            meeting.types.replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace(" ", "")
            .split(",")
        )

        for code in meeting_types:
            if code:
                meeting_sub_type = MeetingSubType.objects.get(code=code)
                meeting.sub_types.add(meeting_sub_type)

        meeting_day = MeetingDay.objects.get(value=meeting.day)
        meeting.days.add(meeting_day)
        meeting.description = meeting.detail
        meeting.published = True
        if 'physical' in meeting.title.lower() and 'online' in meeting.title.lower():
            meeting.type="HYB"   

        if 'hybrid' in meeting.title.lower():
            meeting.type="HYB"   
    
        
        meeting.slug = slugify(f'{meeting.title} {meeting.time} {meeting.type} {meeting.id}')
        
        meeting.save()





class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0019_auto_20210217_1656"),
    ]

    operations = [
        migrations.RunPython(create_meeting_references),
        migrations.RunPython(migrate_physical_meeting_data),
       
    ]
