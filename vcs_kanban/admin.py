from datetime import datetime
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.db.models import Count
from .models import Track, JobToTrack, JobOrder,ViewJobOrder

# Register your models here.
class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'rJOB_NO',
        'rCPART_NO',
        'rCT',
        'rAC_CT',
        'rSTARTDATE',
        'rENDDATE',
        'rUSER_ID',
        'rSTATUS',
        'rACT_STARTDATE',
        'rSTOPDATE',
        'rSTEP',
        'rWORK_NAME',
    )
    pass


class JobToTrackAdmin(admin.ModelAdmin):
    search_fields = (
        # 'JOB202307/0260 '
        "rJOB_NO",
    )

    list_display = (
        'rJOB_NO',
        'rKANBAN',
        'rSTATUS',
    )

    list_filter = (
        'rSTATUS',
    )

    fields =(
        "rJOB_NO",
    )
    pass

class JobOrderAdmin(admin.ModelAdmin):
    search_fields = (
        'rJOB_NO',
        'rPART_NO',
    )

    list_display = (
        'view_job_no',
    )

    list_filter = (
        'rOPEN_DATE',
        'rMTM_DATE',
        'rUSER_ID',
        'rSTATUS',
        'rRMTM_DATE',
        'rSTATUS',
    )

    fields = (
        'rPART_NO',
        'rPLANT',
        'rNQTY',
        'rOPEN_DATE',
        'rMTM_DATE',
        'rUSER_ID',
        'rSTATUS',
        'rRMTM_DATE',
    )

    def view_job_no(self, obj):
        print(obj)
        queryset = Track.objects.values('rPART_NO').filter(
            rJOB_NO=obj.rJOB_NO).annotate(total_count=Count('rPART_NO'))
        print(queryset)
        return queryset
    
    list_per_page = 10
    pass

class ViewJobOrderAdmin(admin.ModelAdmin):
    # change_form_template = "kanban/change_form.html"
    search_fields = (
        'jobno',
    )

    list_display = (
        "jobno",
        "ctn",
        "start_at",
        "end_at",
        "userid",
        "status",
    )

    list_filter = (
        "start_at",
        "end_at",
        "status",
    )

    fieldsets = [
        (
            None,
            {
                "fields": ["jobno", "ctn",],
            },
        ),
        (
            "Action At",
            {
                "classes": ["show"],
                "fields": ["start_at","end_at","userid",],
            },
        ),
        (
            "Action By",
            {
                "fields": ["status",],
            },
        ),
    ]


    def has_delete_permission(self, request, obj=None):
        return False
    
    # def response_change(self, request, object):
    #     if "_reset-kanban" in request.POST:
    #         print("Received")
    
    def save_model(self, request, obj, form, change):
        # print(obj.jobno)
        # print(obj.status)
        ## Step 1.
        Track.objects.filter(rJOB_NO=obj.jobno, rSTATUS=0).update(
            rAC_CT="0",
            rENDDATE=datetime.now(),
            rUSER_ID=None,
            rSTATUS=obj.status,
            rACT_STARTDATE=datetime.now(),
        )
        ## Step 2.
        JobOrder.objects.filter(rJOB_NO=obj.jobno).update(
            rMTM_DATE=datetime.now(),
            rSTATUS=0,
        )
        ## Step 3.
        JobToTrack.objects.filter(rJOB_NO=obj.jobno).update(
            rSTATUS=obj.status,
        )

    readonly_fields = ["jobno", "ctn", "start_at", "end_at", "userid",]
    empty_value_display = "-"
    list_per_page = 25
    
    pass


# admin.site.register(Track, TrackAdmin)
# admin.site.register(JobToTrack,JobToTrackAdmin)
admin.site.register(ViewJobOrder, ViewJobOrderAdmin)
# admin.site.register(JobOrder,JobOrderAdmin)
# admin.site.unregister(Group)
# admin.site.unregister(User)