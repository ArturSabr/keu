# Generated by Django 4.1.7 on 2023-03-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.page')),
            ],
            bases=('app.page',),
        ),
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
