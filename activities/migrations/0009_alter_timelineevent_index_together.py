# Generated by Django 4.1.4 on 2023-01-14 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_announcement"),
        ("activities", "0008_state_and_post_indexes"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="timelineevent",
            index_together={
                ("identity", "type", "subject_post", "subject_identity"),
                ("identity", "type", "subject_identity"),
                ("identity", "created"),
            },
        ),
    ]
