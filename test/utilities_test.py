#this is the "test/utils_test.py" file 


from app.utilities import to_usd


def test_tousd():
    #it rounds to two decimal places and has a dollar sign:  
    assert to_usd(123456789.98) == "$123,456,789.98"
    #it rounds to two decimal places:
    assert to_usd(0.455555) == "$0.46"