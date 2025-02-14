# Generated by Django 4.2.18 on 2025-02-12 19:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0667_encrypt_feature_flag_config"),
    ]

    operations = [
        migrations.CreateModel(
            name="HostDefinition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=posthog.models.utils.UUIDT, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("host", models.CharField(max_length=400)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("last_seen_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "project",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="host_definitions",
                        related_query_name="host_definition",
                        to="posthog.project",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="host_definitions",
                        related_query_name="host_definition",
                        to="posthog.team",
                    ),
                ),
            ],
            options={
                "db_table": "posthog_hostdefinition",
                "indexes": [
                    models.Index(fields=["project", "host"], name="hostdefinition_project_idx"),
                    models.Index(fields=["team", "host"], name="hostdefinition_team_idx"),
                ],
            },
        ),
        migrations.AlterUniqueTogether(
            name="hostdefinition",
            unique_together={("team", "host")},
        ),
        migrations.AddConstraint(
            model_name="hostdefinition",
            constraint=posthog.models.utils.UniqueConstraintByExpression(
                expression="(coalesce(project_id, team_id), host)",
                name="hostdefinition_coalesced_idx",
                concurrently=False,  # New table, this will lock for milliseconds only
            ),
        ),
    ]
