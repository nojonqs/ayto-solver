# Generated by Django 4.1.1 on 2022-09-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BaseMatch",
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
                (
                    "match_state",
                    models.TextField(
                        choices=[
                            ("unknown", "Unknown"),
                            ("no match", "No Match"),
                            ("perfect match", "Perfect Match"),
                        ]
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("name", models.CharField(max_length=80)),
                (
                    "sex",
                    models.TextField(choices=[("male", "Male"), ("female", "Female")]),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Female",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="frontend.person",
                    ),
                ),
            ],
            bases=("frontend.person",),
        ),
        migrations.CreateModel(
            name="Male",
            fields=[
                (
                    "person_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="frontend.person",
                    ),
                ),
            ],
            bases=("frontend.person",),
        ),
        migrations.CreateModel(
            name="NoMatch",
            fields=[
                (
                    "basematch_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="frontend.basematch",
                    ),
                ),
            ],
            bases=("frontend.basematch",),
        ),
        migrations.CreateModel(
            name="PerfectMatch",
            fields=[
                (
                    "basematch_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="frontend.basematch",
                    ),
                ),
            ],
            bases=("frontend.basematch",),
        ),
        migrations.AddField(
            model_name="basematch",
            name="female",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="frontend.female"
            ),
        ),
        migrations.AddField(
            model_name="basematch",
            name="male",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="frontend.male"
            ),
        ),
    ]
