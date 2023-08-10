from django.db import models
from django.db.models import Count

# Create your models here.
class JobToTrack(models.Model):
    rJOB_NO = models.CharField(primary_key=True, max_length=50, verbose_name="Job No.",db_column="JOB_NO", editable=False)
    rKANBAN = models.TextField(verbose_name="Kanban",db_column="KANBAN")
    rSTATUS = models.IntegerField(verbose_name="Status",db_column="STATUS") #int NULL,

    def __str__(self) -> str:
        return f"{self.rKANBAN}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "JOBTOTRACK"
        app_label = "vcs_kanban"
        verbose_name = "ข้อมูล JOB TO TRACK"
        verbose_name_plural = "JOB TO TRACK"

class JobOrder(models.Model):
    rJOB_NO = models.CharField(primary_key=True,max_length=50, verbose_name="Job No.",db_column="JOB_NO", editable=False)
    rPART_NO = models.CharField(max_length=50, verbose_name="Part No.",db_column="PART_NO")
    rPLANT = models.CharField(max_length=10, verbose_name="Plant", db_column="PLANT")
    rNQTY = models.CharField(verbose_name="Qty.",max_length=10, db_column="NQTY")
    rOPEN_DATE = models.DateTimeField(verbose_name="Open At" ,db_column="OPEN_DATE")
    rMTM_DATE = models.DateTimeField(verbose_name="MTM Date",db_column="MTM_DATE")
    rUSER_ID = models.IntegerField(verbose_name="User ID",db_column="USER_ID")
    rSTATUS = models.IntegerField(verbose_name="Status",db_column="STATUS")
    rRMTM_DATE = models.DateTimeField(verbose_name="RMTM Date",db_column="RMTM_DATE")

    def __str__(self) -> str:
        return self.rJOB_NO

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "JOBORDER"
        app_label = "vcs_kanban"
        verbose_name = "ข้อมูล JOB ORDER"
        verbose_name_plural = "JOB ORDER"

class Track(models.Model):
    rKANBAN = models.TextField(max_length=200,verbose_name="KANBAN", db_column="KANBAN")# KANBAN nchar(200) COLLATE Thai_BIN NULL,
    rJOB_NO = models.CharField(max_length=200, verbose_name="JOB NO", db_column="JOB_NO")
    rPART_NO = models.CharField(max_length=30,verbose_name="PART NO", db_column="CPART_NO")# CPART_NO nchar(30) COLLATE Thai_BIN NULL,
    rSTEP = models.IntegerField(verbose_name="STEP", db_column="STEP")# STEP int NULL,
    rWORK_NAME = models.CharField(max_length=50,verbose_name="WORK NAME", db_column="WORK_NAME")# WORK_NAME nchar(50) COLLATE Thai_BIN NULL,
    rCT = models.IntegerField(verbose_name="CT", db_column="CT")# CT int NULL,
    rAC_CT = models.CharField(max_length=50,verbose_name="AC CT", db_column="AC_CT")# AC_CT nvarchar(50) COLLATE Thai_BIN NULL,
    rSTARTDATE = models.DateTimeField(verbose_name="START AT", db_column="STARTDATE")# STARTDATE datetime NULL,
    rENDDATE = models.DateTimeField(verbose_name="END DATE", db_column="ENDDATE")# ENDDATE datetime NULL,
    rUSER_ID = models.CharField(max_length=10, verbose_name="USER ID", db_column="USER_ID")# USER_ID nchar(10) COLLATE Thai_BIN NULL,
    rSTATUS = models.IntegerField(verbose_name="STATUS", db_column="STATUS")# STATUS int DEFAULT 0 NOT NULL,
    rACT_STARTDATE = models.DateTimeField(verbose_name="ACTION AT", db_column="ACT_STARTDATE")# ACT_STARTDATE datetime NULL,
    rSTOPDATE = models.DateTimeField(verbose_name="STOP AT", db_column="STOPDATE")# STOPDATE datetime NULL,
    rSTOP_CT = models.IntegerField(verbose_name="STOP CT", db_column="STOP_CT", default=0)# STOP_CT int DEFAULT 0 NOT NULL,
    rTYPE_USER = models.IntegerField(verbose_name="TYPE USER", db_column="TYPE_USER", default=0)# TYPE_USER int DEFAULT 0 NOT NULL

    def __str__(self) -> str:
        return f"{self.rJOB_NO} => {self.rCPART_NO}"

    class Meta:
        # db_table_comment = "formula_vcst"
        db_table = "TRACK"
        app_label = "vcs_kanban"
        verbose_name = "ข้อมูล TRACK"
        verbose_name_plural = "TRACK"

STATUS_CHOICES = (
    (0, "กำลังดำเนินการ"),
    (1, "ยกเลิก"),
)


class ViewJobOrder(models.Model):
    jobno = models.CharField(primary_key=True,max_length=20, verbose_name="เลขที่เอกสาร", db_column="jobno", editable=True)
    ctn = models.IntegerField(verbose_name="จำนวน",db_column="ctn")
    start_at = models.DateTimeField(verbose_name="เริ่มทำงาน",db_column="start_at")
    end_at = models.DateTimeField(verbose_name="สิ้นสุดที่",db_column="end_at")
    userid = models.CharField(verbose_name="แก้ไขโดย",max_length=20,db_column="userid")
    status = models.IntegerField(verbose_name="สถานะ",choices=STATUS_CHOICES,db_column="status")

    def __str__(self) -> str:
        return self.jobno
        

    class Meta:
        managed = False
        db_table = "view_tracking"
        app_label = "vcs_kanban"
        verbose_name = "จัดการข้อมูล TRACK"
        verbose_name_plural = "TRACK"
