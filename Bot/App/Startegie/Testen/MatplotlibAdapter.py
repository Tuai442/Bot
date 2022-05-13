import matplotlib.dates as mdates

class MathplotlibAdapter:
    def __init__(self):
        pass


    def add_rect_shape(self, ax, y1, y2, color: str, opacity: float =0.4, width: int =0):
        ax.axhspan(y1, y2, alpha=opacity, color=color)


    def add_annotations(self, ax, date_index: int, y: float, text: str, font_color: str ="black", arrow_color: str ="black", bg_color: str =None):
        ax[0].annotate(text, (date_index, y), fontsize=20, xytext=(date_index +10, y+10),
                           color='r',
                           arrowprops=dict(
                               arrowstyle='->',
                               facecolor='r',
                               edgecolor='r'))

