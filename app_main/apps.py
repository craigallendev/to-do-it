from django.apps import AppConfig


class AppMainConfig(AppConfig):
    # Set the default type of primary key fields for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'
    # Define the name of the app. 
    # This is used to reference the app within Django.
    name = 'app_main'
