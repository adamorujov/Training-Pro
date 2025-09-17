from django.core.management.base import BaseCommand
from django.conf import settings
from modeltranslation.translator import translator


class Command(BaseCommand):
    help = "Copy old field values into default translation fields for all registered models"

    def handle(self, *args, **options):
        default_lang = settings.LANGUAGE_CODE.split("-")[0]  # məsələn 'az', 'en'
        self.stdout.write(self.style.WARNING(f"Default language: {default_lang}"))

        # bütün translation model-ləri alırıq
        for model in translator.get_registered_models():
            model_name = model.__name__
            opts = translator.get_options_for_model(model)  # TranslationOptions
            fields = opts.fields   # tuple

            self.stdout.write(self.style.WARNING(f"Processing model: {model_name}"))

            for obj in model.objects.all():
                updated = False
                for field in fields:
                    translated_field = f"{field}_{default_lang}"
                    if hasattr(obj, field) and hasattr(obj, translated_field):
                        value = getattr(obj, field)
                        if value:  # dəyər varsa, həmişə kopyala
                            setattr(obj, translated_field, value)
                            updated = True
                if updated:
                    obj.save()

            self.stdout.write(self.style.SUCCESS(f"✔ Done for {model_name}"))
