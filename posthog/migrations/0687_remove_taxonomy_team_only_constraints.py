# Generated by Django 4.2.18 on 2025-03-13 10:33

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False  # Because revert contains CURRENTLY

    dependencies = [
        ("posthog", "0686_alter_errortrackingissue_status"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="eventproperty",
            name="posthog_event_property_unique_team_event_property",
        ),
        migrations.RemoveConstraint(
            model_name="propertydefinition",
            name="posthog_propertydefinition_uniq",
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterUniqueTogether(
                    name="eventdefinition",
                    unique_together=set(),
                ),
            ],
            database_operations=[
                # Using RunSQL just to work around a decade-old bug in Django's sqlmigrate failing @ AlterUniqueTogether
                # https://code.djangoproject.com/ticket/26624
                migrations.RunSQL(
                    "ALTER TABLE posthog_eventdefinition DROP CONSTRAINT posthog_eventdefinition_team_id_name_80fa0b87_uniq",
                    reverse_sql="ALTER TABLE posthog_eventdefinition ADD CONSTRAINT posthog_eventdefinition_team_id_name_80fa0b87_uniq UNIQUE (team_id, name)",
                ),
            ],
        ),
    ]
