import string

displayable_charset = string.digits + string.letters + string.punctuation + ' '

"""
https://sso.americanexpress.com/SSO/request?request_type=un_createid&ssolang=en_NL&inav=at_sitefooter_register
"""
amex_charset = string.digits + string.lowercase + '%&_?#=-'

_boa_blacklist = '$<>&^![] '
boa_charset = ''.join(ch for ch in (string.digits + string.letters + string.punctuation) if ch not in _boa_blacklist)

"""
https://fps.fidelity.com/ftgw/Fps/pages/SharedExp/defaultWeb/common2/scripts/validation.js

jQuery.validator.addMethod("pinAlphanumeric", function(value, element) {
        return this.optional(element) || /^[a-z0-9]+$/i.test(value);
}, "Please enter a valid password");
"""
fidelity_charset = string.digits + string.letters


"""
https://chaseonline.chase.com/js/EandAValidations.js

function isValidPassword(formElt, isRSA, ShouldCheckForSpecialCharacters) {
    var txtPwd = ge(formElt).value;
    var pwdLength = txtPwd.length;
    if (pwdLength == 0) {
        return setResult(false, "errTRpwd", "errSpanpwd", "Please enter a Password.", 'txtPassword');
    }
    else if (pwdLength > 0) {
        if (isRSA=="True" || isRSA=="true") {
            if (pwdLength < 7 || pwdLength > 8) {
                return setResult(false, "errTRpwd", "errSpanpwd", "Your Password must be between 7 & 8 characters. Please re-create your Password.", formElt);
            }
            else {
                setResult(true, "errTRpwd", "errSpanpwd", "", formElt);
            }

            if (/\W/.test(txtPwd)) {
                return setResult(false, "errTRpwd", "errSpanpwd", "Special characters <br>(e.g. #,@,$) are not allowed", 'txtPassword');
            }
            else {
                return setResult(true, "errTRpwd", "errSpanpwd", "", 'txtPassword');
            }
        }
        else {
            if (pwdLength < 7) {
                return setResult(false, "errTRpwd", "errSpanpwd", "Minimum 7 characters are required.", formElt);
            }
            else {
                setResult(true, "errTRpwd", "errSpanpwd", "", formElt);
            }

            if (ShouldCheckForSpecialCharacters == "True" || ShouldCheckForSpecialCharacters == "true") {
               if (/[^a-zA-Z0-9!#$%')(*+,-.:;=?@\/\]\[^_`}{|~\\]/.test(txtPwd))
               {
                   return setResult(false, "errTRpwd", "errSpanpwd", invalidPasswordch, 'txtPassword');
                }
                else {
                    return setResult(true, "errTRpwd", "errSpanpwd", "", 'txtPassword');
                }
            }
            else {
                if (/\W/.test(txtPwd)) {
                    return setResult(false, "errTRpwd", "errSpanpwd", "Special characters <br>(e.g. #,@,$) are not allowed", 'txtPassword');
                }
                else {
                    return setResult(true, "errTRpwd", "errSpanpwd", "", 'txtPassword');
                }
            }

        }
    }


    if (txtPwd.length > 0) {
        if (hasOnlyNumbers(txtPwd)) {
            return setResult(false, "errTRpwd", "errSpanpwd", "Password must have at least one letter", 'txtPassword');
        }
        else {
            setResult(true, "errTRpwd", "errSpanpwd", "", 'txtPassword');
        }
    }
    if (pwdLength > 0) {
        if (hasOnlyCharacters(txtPwd)) {
            return setResult(false, "errTRpwd", "errSpanpwd", "Password must have at least one number", 'txtPassword');
        }
        else {
            setResult(true, "errTRpwd", "errSpanpwd", "", 'txtPassword');
        }
    }


    return true;
}

"""
chase_charset = string.letters + string.digits + r'''!#$%')(*+,-.:;=?@/][^_`}{|~\\'''
