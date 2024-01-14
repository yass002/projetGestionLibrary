from django.apps import AppConfig


class MylibrarydataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "MyLibraryData"

    def ready(self):
        import MyLibraryData.Signal