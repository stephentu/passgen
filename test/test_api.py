from passgen.api import google, amex, boa, fidelity, chase

def test_api_simple():
    # just test to make sure it doesn't crash
    apis = (google, amex, boa, fidelity, chase)
    for api in apis:
        g = api()
        assert g.generate(urandom=True)
