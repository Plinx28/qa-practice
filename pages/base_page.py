class BasePage:
    url = None

    def __init__(self, page) -> None:
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            raise NotImplementedError("Не указан URL страницы в классе")
