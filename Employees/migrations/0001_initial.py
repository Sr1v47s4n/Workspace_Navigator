# Generated by Django 4.1 on 2023-02-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("adminUsername", models.CharField(max_length=65, unique=True)),
                ("adminName", models.CharField(max_length=65)),
                ("adminPhNo", models.CharField(max_length=15)),
                ("adminEmail", models.CharField(max_length=85)),
                ("usrCode", models.CharField(max_length=85)),
            ],
            options={
                "verbose_name_plural": "Admins",
            },
        ),
        migrations.CreateModel(
            name="EmployeeData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("staffName", models.CharField(max_length=60)),
                ("staffDob", models.DateField()),
                ("staffId", models.CharField(max_length=60)),
                ("staffBranch", models.CharField(max_length=65)),
                ("staffExp", models.CharField(max_length=65)),
                ("staffSalary", models.CharField(max_length=65)),
                ("staffPhNo", models.CharField(max_length=15)),
                ("staffEmail", models.CharField(max_length=50)),
                ("staffQualification", models.CharField(max_length=50)),
                ("usrCode", models.CharField(max_length=85)),
            ],
            options={
                "verbose_name_plural": "Staffs",
            },
        ),
    ]
