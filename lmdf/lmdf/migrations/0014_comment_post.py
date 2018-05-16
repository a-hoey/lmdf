# Generated by Django 2.0.4 on 2018-05-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lmdf', '0013_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lmdf.Diagnosis'),
            preserve_default=False,
        ),
    ]