import pprint
import time

import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib import animation

from Bot.App.Startegie.Testen.MatplotlibAdapter import MathplotlibAdapter
from Bot.App.Startegie.Testen.fetchSimulator import Fetch


class Simulator:
    def __init__(self, agent, fetch, date):
        self.agent = agent
        self.fetch = fetch
        self.adapter = MathplotlibAdapter()

        self.fig = mpf.figure(figsize=(15,20))
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ax2 = self.ax1.twinx()
        self.ax_list = None
        self.isLevel = False

        # mpf.plot(data, type='line', ax=self.ax2, axtitle='Simulatie', xrotation=0, style="yahoo")



    def start(self, speed=0.5):
        self.speed = speed
        ani = animation.FuncAnimation(self.fig, self.animate, fargs=(self.ax2, ), interval=1)
        plt.show()

    def animate(self, _, ax):
        time.sleep(self.speed)

        # Data ophalen
        new_data = self.fetch.next()
        self.agent.next(new_data)

        total_data = self.fetch.get_total_fetched_data()
        _ , self.ax_list = mpf.plot(total_data, ax=ax, style='yahoo', type="line", returnfig=True)

        graph = self.agent.get_graph()
        self.process_graph_data(ax, graph)

        print("=================================")
        # pprint.pprint(graph)


        # self.plot(total_data, graph, ax)


    def plot(self, total_data, graph, ax):
        mpf.plot(total_data, ax=ax, style='yahoo', type="line",)

    def process_graph_data(self, ax, graph):
        for key in graph.keys():
            if key == "levels":
                if self.isLevel is False:
                    first = True
                    previous = None
                    for level in graph["levels"]:
                        data = graph["levels"][level]
                        if first:
                            previous = data
                            y1 = data["y"][0]
                            y2 = data["y"][1]
                            first = False
                        else:
                            y1 = previous["y"][1]
                            y2 = data["y"][0]
                            previous = data

                        self.adapter.add_rect_shape(ax, y1, y2, data["background-color"],)
                    self.isLevel = True

                # bounces
                for level in graph["levels"]:
                    for bounce in graph["levels"][level]["bounces"]:
                        date_index = self.fetch.get_index_from_date(bounce[0])
                        self.adapter.add_annotations(self.ax_list, date_index, bounce[1], "bounce")


