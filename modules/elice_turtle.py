"""
ps. 템플릿에 bash 커맨드 자꾸 초기화되는데 확인 부탁드립니다 저만 그런가요
"""

from turtle import *
import sys
import time

class EducationalMethod:
    """
    교육용 컨텐츠 베이스 클래스
    함수명은 되도록 매뉴얼 따라서 재정의 해주세요 (본판이 좀 많이 중구난방입니다)
    Error 클래스 외의 Exception은 추가 논의 중입니다(스크린 밖으로 이탈 등)
    """
    def __init__(self):
        self.error = {}
        self._error_occurred = False
        self.e_idx = [False] * 10
        self.error_line_number = -1

    def execute(self):
        if not self._try():
            self._behave()
        self._terminate()

    def _try(self):
        for _exception, _err_message in self.error.items():
            if _exception:
                print(_err_message)
                self._error_occurred = True
        return self._error_occurred

    def _behave(self):
        pass

    def _terminate(self):
        pass

class Go(EducationalMethod):
    """
    Turtle.forward()
    """
    def __init__(self, d):
        super().__init__()
        self.d = d
        try:
            forward(d)
        except (SyntaxError, TypeError, NameError) as e:
            _, __, e_traceback = sys.exc_info()
            self.error_line_number = e_traceback.tb_lineno
            if isinstance(e, SyntaxError):
                self.e_idx[0] = True
            elif isinstance(e, TypeError):
                if type(d) is str:
                    self.e_idx[1] = True
                else:
                    self.e_idx[2] = True
            elif isinstance(e, NameError):
                self.e_idx[3] = True

        self.error = {
            self.e_idx[0]: "go() 함수를 실행할 때 문제가 생겼네요! 다시 한 번 확인해 볼까요?",
            self.e_idx[1]: f"go() 함수는 숫자가 필요한 데 문자열인 {d}가 들어왔네요? 거북이는 혼란스러워요ㅠㅠ",
            self.e_idx[2]: f"\"{d}만큼 앞으로 가!\"가 어떤 의미인지 거북이는 모르겠어요...",
            self.e_idx[3]: "변수의 이름을 한 번 다시 확인해볼까요?"
        }

    def _behave(self):
        forward(self.d)

    def _terminate(self):
        if not is_turtle_on_screen():
            print("음...어?")
            time.sleep(1)
            print("거북이가 어디로 갔죠?")
            time.sleep(1)
            print("엥?")

def go(distance):
    g = Go(distance)
    g.execute()

# def go(distance:int):
#     forward(distance)

# def turn_left(angle:int):
#     left(angle)

# def turn_right(angle:int):
#     right(angle)

# def move(x_coord:int,y_coord:int):
#     setpos(x_coord, y_coord)

# def jump(x_coord:int,y_coord:int):
#     pu()
#     setpos(x_coord,y_coord)
#     pd()

# def spot(x_coord:int,y_coord:int):
#     c = Turtle()
#     c.hideturtle()
#     c.color("red")
#     c.pu()
#     c.setpos(x_coord,y_coord)
#     c.pd()
#     c.dot(20,"red")
#     del c


def is_turtle_on_screen(): # 1024x768
    x, y = pos()
    if -512 <= x <= 512 and -384 <= y <= 384:
        return True
    else:
        return False

def 거북이입장():
    screen = Screen()
    pensize(7)
    shape("turtle")
    screen.setup(width=1024, height=768)
    screen.setup(1.0, 1.0)

if __name__ == "__main__":
    pass
