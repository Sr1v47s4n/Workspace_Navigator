from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class AdminData(AbstractBaseUser):
    adminUsername = models.CharField(null=False, max_length=65, unique=True)
    adminName = models.CharField(null=False, max_length=65)
    adminPhNo = models.CharField(null=False, max_length=15)
    adminEmail = models.CharField(null=False, max_length=85)
    usrCode = models.CharField(null=False, max_length=85)
    objects = BaseUserManager()

    USERNAME_FIELD = "adminUsername"
    REQUIRED_FIELDS = ["adminName", "adminPhNo", "adminEmail", "usrCode"]

    def __str__(self):
        return f"{self.adminName}"

    class Meta:
        verbose_name_plural = "Admins"


class EmployeeData(models.Model):
    staffName = models.CharField(max_length=60, null=False)
    staffDob = models.DateField(null=False)
    staffId = models.CharField(max_length=60, null=False)
    staffBranch = models.CharField(null=False, max_length=65)
    staffExp = models.CharField(null=False, max_length=65)
    staffSalary = models.CharField(null=False, max_length=65)
    staffPhNo = models.CharField(max_length=15, null=False)
    staffEmail = models.CharField(max_length=50, null=False)
    staffQualification = models.CharField(max_length=50, null=False)
    usrCode = models.CharField(null=False, max_length=85)

    def __str__(self):
        return f"{self.staffName}"

    class Meta:
        verbose_name_plural = "Staffs"
