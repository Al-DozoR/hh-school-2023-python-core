from hw.logger import Logger


@Logger
class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {} if wines is None else {wine.title: wine for wine in wines}
        self.beers = {} if beers is None else {beer.title: beer for beer in beers}

    """
    Проверяет наличие напитка в магазине за О(1)

    :param title:
    :return: True|False
    """

    def has_drink_with_title(self, title=None) -> bool:
        return title in self.wines or title in self.beers

    """
    Метод получения списка напитков (вина и пива) отсортированных по title

    :return: list
    """

    def get_drinks_sorted_by_title(self) -> list:
        all_drinks = list(self.wines.values()) + list(self.beers.values())
        return sorted(all_drinks, key=lambda drink: drink.title)

    """
    Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

    :return: list
    """

    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        filtered_drinks = []
        for drink_dict in [self.wines, self.beers]:
            for drink in drink_dict.values():
                if from_date and drink.production_date < from_date:
                    continue
                if to_date and drink.production_date > to_date:
                    continue
                filtered_drinks.append(drink)
        return filtered_drinks
