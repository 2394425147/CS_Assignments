class Clock:
    def __init__(self):
        self._hour = 0
        self._minute = 0
        self._second = 0
        pass

    def show_time(self):
        print(f"{self._hour:02}:{self._minute:02}:{self._second:02}")
        pass

    def set_time(self, hour: int, minute: int, second: int):
        if hour < 0:
            print(f"请确认{hour}小时大于0")
            return

        if minute < 0 or minute > 59:
            print(f"请确认{minute}分钟大于0并小于60")
            return

        if second < 0 or second > 59:
            print(f"请确认{second}秒数大于0并小于60")
            return

        self._hour = hour
        self._minute = minute
        self._second = second
        pass
