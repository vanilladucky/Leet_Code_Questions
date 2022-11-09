class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        days_before = 1
        while self.prices and price >= self.prices[-1][0]:
            days_before+=self.prices.pop()[1]
        self.prices.append([price,days_before])
        return days_before
