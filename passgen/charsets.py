import string

displayable_charset = string.digits + string.letters + string.punctuation + ' '

"""
https://sso.americanexpress.com/SSO/request?request_type=un_createid&ssolang=en_NL&inav=at_sitefooter_register
"""
amex_charset = string.digits + string.lowercase + '%&_?#=-'
