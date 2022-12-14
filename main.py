from diaries.DiarySample import DiarySample
from diaries.SatoDiary import SatoDiary
from diaries.MorishigeDiary import MorishigeDiary
from diaries.ShimizuDiary import ShimizuDiary



# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
            SatoDiary(),
            MorishigeDiary(),
            ShimizuDiary(),] 


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()