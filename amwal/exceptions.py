class StockNumberNotFoundError(Exception):
    def __init__(self, stock_number):
        super().__init__(
            f"Can't find stock number {stock_number} in the Boursa listing"
        )


class TickerNotFoundError(Exception):
    def __init__(self, ticker):
        super().__init__(f"Can't find {ticker} in the Boursa listing")


class MalformedCorpIdentifierError(Exception):
    def __init__(self, ident):
        super().__init__(f"{ident} is neither a well-formed ticker nor a stock number")


class MalformedDateStringError(Exception):
    def __init__(self, date):
        super().__init__(
            f"{date} is not a well-formed date string, please use the format DD/MM/YYYY"
        )
