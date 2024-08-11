from django.db import migrations


def load_root_user(apps, schema_editor):
    from django.core.management import call_command

    call_command("loaddata", "root_user.json")


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(load_root_user),
    ]
