# Generated by Django 4.0.3 on 2022-03-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_question_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom complet')),
                ('email', models.CharField(max_length=255, verbose_name='E-Mail')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='âge')),
            ],
        ),
    ]
