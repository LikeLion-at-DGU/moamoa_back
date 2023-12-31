# Generated by Django 4.2.4 on 2023-08-13 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='boards',
        ),
        migrations.RemoveField(
            model_name='store',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='store',
            name='menus',
        ),
        migrations.RemoveField(
            model_name='store',
            name='reviews',
        ),
        migrations.AddField(
            model_name='board',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='main.store'),
        ),
        migrations.AddField(
            model_name='chat',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chats', to='main.store'),
        ),
        migrations.AddField(
            model_name='menu',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='main.store'),
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.store'),
        ),
    ]
