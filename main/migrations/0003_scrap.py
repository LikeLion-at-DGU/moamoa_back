# Generated by Django 4.2.4 on 2023-08-13 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_store_boards_remove_store_chat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_scraped', models.DateTimeField(default=django.utils.timezone.now)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scraps', to='main.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'store')},
            },
        ),
    ]
