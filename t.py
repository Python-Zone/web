
class BangFuRen(models.Model):
    bangfu_name = models.CharField(max_length=100)
    company = models.CharField(max_length=200, blank=True, null=True)
    relation = models.CharField(max_length=100, blank=True, null=True)
    call_number = models.CharField(max_length=36, blank=True, null=True)
    pinkunhus = models.ManyToManyField(PinKunHu, related_name="bangfurens")

    class Meta:
        verbose_name_plural = "帮扶人"


