
class PlotlyAdapter:
    def __init__(self):
        self._plot = {
            "shapes": list(),
            "annotations": list()
        }

    def add_rect_shape(self, p1: tuple, p2: tuple, color: str, opacity: float =0.2, width: int =0):
        x_0, y_0 = p1
        x_1, y_1 = p2
        self._plot["shapes"].append({
            "type": "rect",
            "xref": "x",
            "yref": "y",
            "x0": x_0,
            "y0": y_0,
            "x1": x_1,
            "y1": y_1,
            "fillcolor": color,
            "opacity": opacity,
            "line": {
                "width": width
            }
        })

    def reset_rect_shape(self):
        self._plot["shapes"] = list()

    def add_layout(self, layout: dict):
        pass

    def shapes(self):
        pass

    def add_annotations(self, p1: tuple, text: str, font_color: str ="black", arrow_color: str ="black", bg_color: str =None):
        x, y = p1
        self._plot["annotations"].append({
            "x": x,
            "y": y,
            "xref": 'x',
            "yref": 'y',
            "text": text,
            "font": {"color": font_color},
            "showarrow": True,
            "xanchor": 'right',
            "arrowcolor": arrow_color,
            "ax": 0,
            "ay": -25,
            "bordercolor": '#c7c7c7',
            "borderwidth": 2,
            "borderpad": 4,
            "bgcolor": bg_color,
            "opacity": 0.8
        })

    def delete_key(self, key: str):
        if key in self._plot.keys():
            self._plot[key] = list()

    def key_exists(self, key: str) -> bool:
        if key in self._plot.keys():
            return True
        return False

    @property
    def plot(self):
        return self._plot
