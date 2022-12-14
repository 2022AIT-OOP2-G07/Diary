from diaries.AbstractDiary import AbstractDiary

class ShimizuDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-13"

    def get_summary(self):
        return "昨日バイトだったが、忘れていた。今度お詫びの品を持っていこうと思う。"

    def get_author(self):
        return "しみず"