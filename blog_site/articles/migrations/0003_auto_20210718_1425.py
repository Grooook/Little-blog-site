# Generated by Django 3.2.5 on 2021-07-18 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_auto_20210717_1504'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'managed': True, 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Coment', 'verbose_name_plural': 'Coments'},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]