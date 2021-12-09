from django.db import models

class ReadTagsOrder(models.Model):
    
    scan_time = models.DateTimeField()

    def __str__ (self):
        return "Read at: " + str(self.scan_time)
    

class Tag(models.Model):
    
    strEPC = models.CharField(max_length=100)
    antenna = models.IntegerField()
    strRSSI = models.CharField(max_length=100)
    nReadCount = models.IntegerField()
    
    readtagorder = models.ForeignKey(ReadTagsOrder, on_delete=models.CASCADE)

    def __str__(self):
        return self.strEPC + " - " + str(self.readtagorder)