from django.db import models


class Customer(models.Model):
    CNF_NUM = models.IntegerField()  # customer confirmation number
    MILEAGEPLS_NUM = models.IntegerField()  # customer mileage plus number
    FIRST_NAME = models.CharField(max_length=30)  # Customer first name
    LAST_NAME = models.CharField(max_length=30)  # Customer last name

    def __str__(self):
        return self.CNF_NUM + ' - ' + self.MILEAGEPLS_NUM + ' - ' + self.FIRST_NAME + ' - ' + self.LAST_NAME


class Baggage_Desc(models.Model):
    BAG_ID = models.IntegerField()  # Baggage id
    BAG_CNF_NUM = models.ForeignKey(Customer, related_name='bag_conf_num',
                                    on_delete=models.CASCADE)  # customer confirmation number
    BAG_MILEAGEPLS_NUM = models.ForeignKey(Customer, related_name='bag_mileage_num',
                                           on_delete=models.CASCADE)  # customer mileage number
    WAREHOUSE_BAG_ID = models.IntegerField()  # bag's warehouse id
    BAG_COLOR = models.CharField(max_length=10)  # bag's color
    BAG_SIZE = models.IntegerField()  # bag's size
    BAG_BRAND = models.CharField(max_length=20)  # bag's brand
    KEY_IDENTIF_ITEM = models.BooleanField()  # key identifying item in the bag

    def __unicode__(self):
        return u'%s' % (self.name)


class Report(models.Model):
    REPO_ID = models.IntegerField()  # report id
    REPO_CNF_NUM = models.ForeignKey(Customer, related_name='conf_num',
                                     on_delete=models.CASCADE)  # customer confirmation number
    REPO_MILEAGEPLS_NUM = models.ForeignKey(Customer, related_name='mileage_num',
                                            on_delete=models.CASCADE)  # customer mileage plus number
    BAG_DESC_ID = models.ForeignKey(Baggage_Desc, on_delete=models.CASCADE)  # Bag description id
    REPO_STAT = models.CharField(max_length=10)  # report status
    CUST_EMAIL = models.CharField(max_length=20)  # customer email address
    CUST_PHONE = models.IntegerField()  # customer phone number
    CUST_PERM_ADDR = models.CharField(max_length=50)  # customer permanent address
    CUST_TEMP_ADDR = models.CharField(max_length=50)  # customer temporary address

    def __unicode__(self):
        return u'%s' % (self.name)


class Baggage_Content_Img(models.Model):
    CONTENT_ID = models.IntegerField()  # Content image id
    WAREHOUSE_CONT_ID = models.ForeignKey(Baggage_Desc, on_delete=models.CASCADE)  # warehouse baggage id
    CONTENT_IMG = models.CharField(max_length=100)  # content image address on disk

    def __unicode__(self):
        return u'%s' % (self.name)


class Baggage_Img(models.Model):
    IMG_ID = models.IntegerField()  # Baggage image id
    IMG_CNF_NUM = models.ForeignKey(Customer, related_name='bag_img_conf_num',
                                    on_delete=models.CASCADE)  # customer confirmation number
    IMG_MILEAGEPLS_NUM = models.ForeignKey(Customer, related_name='bag_img_mileage_num',
                                           on_delete=models.CASCADE)  # customer mileage number

    def __unicode__(self):
        return u'%s' % (self.name)
