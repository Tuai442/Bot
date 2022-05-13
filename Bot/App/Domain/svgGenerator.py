from datetime import timedelta, datetime


class SVGgenerator:
    def __init__(self):
        pass

    @classmethod
    def triangle(cls, x, y, side: str):
        pass
        # DOWN:
        # ______
        # \    /
        #  \  /
        #   \/
        #

        # x = datetime.strptime(x, '%Y-%m-%d')
        # x1, y1 = x - timedelta(days=1), y + 50
        # x2, y2 = x, y
        # x3, y3 = x + timedelta(days=1), y + 50
        # # x1, y1 = 0, 50
        # # x2, y2 = 75, 0
        # # x3, y3 = 100, 50
        # if side == "UP":
        #     return "M0 0 L2 4 L4 0 Z"
        # else:
        #     return f"M {x1} {y1} L {x2} {y2} L {x3} {y3}Z"
