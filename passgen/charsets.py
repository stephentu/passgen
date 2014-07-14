import string

displayable_charset = string.digits + string.letters + string.punctuation + ' '

"""
https://sso.americanexpress.com/SSO/request?request_type=un_createid&ssolang=en_NL&inav=at_sitefooter_register
"""
amex_charset = string.digits + string.lowercase + '%&_?#=-'

"""
https://fps.fidelity.com/ftgw/Fps/pages/SharedExp/defaultWeb/common2/scripts/validation.js

        jQuery.validator.addMethod("pinAlphanumeric", function(value, element) {
                return this.optional(element) || /^[a-z0-9]+$/i.test(value);
        }, "Please enter a valid password");
"""
fidelity_charset = string.digits + string.letters
