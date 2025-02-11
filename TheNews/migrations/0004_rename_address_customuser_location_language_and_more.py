# Generated by Django 5.0.7 on 2024-07-19 13:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheNews', '0003_post_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='address',
            new_name='location',
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifie_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='languageCreatedBy', to=settings.AUTH_USER_MODEL)),
                ('modifie_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='languagemodifie_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='TheNews.language'),
        ),
    ]
