from diaries.AbstractDiary import AbstractDiary

class KazahayaDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-14"

    def get_summary(self):
        return "今日も寒い"

    def get_author(self):
        return "さちこ"