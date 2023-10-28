from stock_class import Stock_Data

stock_data = Stock_Data()
valid_ticker = "AMZN"
invalid_ticker = "XYZ"


def test_class_instance():

    instance_status = isinstance(stock_data, Stock_Data)

    assert (instance_status == True)


def test_quote_valid_ticker():

    assert (stock_data.quote(valid_ticker) > 0)

    assert (type(stock_data.quote(valid_ticker)) == float)


def test_invalid_ticker():

    assert (stock_data.quote(invalid_ticker) == 0)
