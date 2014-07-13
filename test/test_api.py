from passgen.api import google, amex, boa

def test_api_simple():
    # just test to make sure it doesn't crash
    apis = (google, amex, boa)
    for api in apis:
        g = api()
        assert g.generate(urandom=True)
