
class PhoneField(CharField):
    default_validators = [phonevalidator.validate_phone_number]
    description = _("Phone number")

    def __init__(self, *args, **kwargs):
        # max_length=20 to be compliant with RFCs 3696 and 5321
        kwargs.setdefault('max_length', 20)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # We do not exclude max_length if it matches default as we want to change
        # the default in future.
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        # As with CharField, this will cause phone validation to be performed
        # twice.
        return super().formfield(**{
            'form_class': forms.PhonelField,
            **kwargs,
        })
