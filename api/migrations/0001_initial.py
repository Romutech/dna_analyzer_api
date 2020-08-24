# Generated by Django 3.1 on 2020-08-24 15:24

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('file_path', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('file', models.TextField(null=True)),
                ('note', models.TextField(null=True)),
                ('nb_bases', models.IntegerField(null=True)),
                ('nb_a', models.IntegerField(null=True)),
                ('nb_c', models.IntegerField(null=True)),
                ('nb_g', models.IntegerField(null=True)),
                ('nb_t', models.IntegerField(null=True)),
                ('percentage_a', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('percentage_c', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('percentage_g', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('percentage_t', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('percentage_gc', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('percentage_at', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date de création')),
                ('dna_walk_graph_data', models.TextField(null=True)),
                ('ratio_g_c_graph_data', models.TextField(null=True)),
            ],
        ),
    ]
