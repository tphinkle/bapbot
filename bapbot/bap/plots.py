## Imports

# Scientific computing
from bokeh.plotting import figure
import bokeh.resources



def create_bapper_bappe_counts_heatmap(bappers, bappees, bap_counts):
    """
    """
    pass


def create_bapper_stats_plot(bappers, bap_counts):
    """
    """
    plot = figure(x_range=bappers, )
    plot.vbar(x=bappers, top=bap_counts, width = 0.1)
    plot_html = bokeh.embed.file_html(plot, bokeh.resources.CDN, title='bapper stats')
    return plot_html


def create_bappee_stats_plot(bappees, bap_counts):
    """
    """
    plot = figure(x_range=bappees, )
    plot.vbar(x=bappees, top=bap_counts, width = 0.1)
    plot_html = bokeh.embed.file_html(plot, bokeh.resources.CDN, title='bapper stats')
    return plot_html
