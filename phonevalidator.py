import re


class PhoneValidator:
    message = _('Enter a valid email address.')
    code = 'invalid'
    user_regex = (
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)')
    domain_regex = (r'\+*\221*7[7860][" "\-]*[0-9]{3}[" "\-]*[0-9]{2}[" "\-]*[0-9]{2}')  
    domain_allowlist = ['localhost']



    def __init__(self, message=None, code=None):
        
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if not value:
            raise ValidationError(self.message, code=self.code, params={'value': value})
        

        if not self.user_regex.match(domain_regex):
            raise ValidationError(self.message, code=self.code, params={'value': value})


validate_phone_number = PhoneValidator()

       
        