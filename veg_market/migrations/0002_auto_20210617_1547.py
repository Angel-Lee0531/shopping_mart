# Generated by Django 3.2.3 on 2021-06-17 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veg_market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField()),
                ('quantity', models.IntegerField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='VegTypes',
            new_name='FoodTypes',
        ),
        migrations.DeleteModel(
            name='Veg',
        ),
        migrations.AddField(
            model_name='food',
            name='foodtypes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veg_market.foodtypes'),
        ),
    ]
