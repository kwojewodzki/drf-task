from django.core.exceptions import ValidationError


def validate_time_to_expire(value):
    """Validates user input of expiration time for link."""
    MIN_TIME = 300
    MAX_TIME = 30000
    if not MIN_TIME <= value <= MAX_TIME:
        raise ValidationError("Value must be a number between 300 and 30000 seconds.")
