# Generated by Django 3.0.7 on 2021-06-29 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_auto_20210629_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-updated_at']},
        ),
    ]