# news/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_title_words(value):
    words = value.split()
    if len(words) < 2:
        raise ValidationError(_("O título deve conter pelo menos 2 palavras."))
