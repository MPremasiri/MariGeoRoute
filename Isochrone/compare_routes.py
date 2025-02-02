import matplotlib.pyplot as plt

import utils.graphics as graphics
import config
from routeparams import RouteParams
from constraints.constraints import *
from weather import WeatherCondCMEMS


if __name__ == "__main__":
    filename1 = "/home/kdemmich/MariData/Code/Figures/Depth10m/min_time_routeroute_10m2.json"
    filename2 = "/home/kdemmich/MariData/Code/Figures/NoDepthConstraint2/no_depth_constraint.json"
    figurefile = "/home/kdemmich/MariData/Code/Figures"
    rp_read1 = RouteParams.from_file(filename1)
    rp_read2 = RouteParams.from_file(filename2)

    ##
    # init wheather
    windfile = config.DEFAULT_GFS_FILE
    model = config.DEFAULT_GFS_MODEL
    start_time = dt.datetime.strptime(config.DEFAULT_GFS_DATETIME, '%Y%m%d%H')
    hours = config.TIME_FORECAST
    lat1, lon1, lat2, lon2 = config.DEFAULT_MAP
    depthfile = config.DEFAULT_DEPTH_FILE
    wt = WeatherCondCMEMS(windfile, model, start_time, hours, 3)
    wt.set_map_size(lat1, lon1, lat2, lon2)
    wt.add_depth_to_EnvData(depthfile)

    ##
    # init Constraints
    water_depth = WaterDepth(wt)
    water_depth.set_drought(20)

    ##
    # plotting routes in depth profile
    fig, ax = plt.subplots(figsize=(12, 7))
    fig, ax = water_depth.plot_constraint(fig, ax)
    #water_depth.plot_route_in_constraint(rp_read, 0, fig, ax)
    rp_read1.plot_route(ax, 'orangered', "10m Tiefgang")
    rp_read2.plot_route(ax, 'cyan', "kein Tiefgang")
    ax.legend()
    plt.savefig(figurefile + '/route_waterdepth.png')

    ##
    # plotting power vs. distance
    fig, ax = plt.subplots(figsize=(12, 8), dpi=96)
    rp_read1.plot_power_vs_dist(graphics.get_colour(0), "10m Tiefgang")
    rp_read2.plot_power_vs_dist(graphics.get_colour(1), "kein Tiefgang")
    ax.legend()
    plt.savefig(figurefile + '/route_power.png')

    ##
    # plotting routes in wind data
    #fig, ax = plt.subplots(figsize=(12, 7))
    #wt.plot_weather_map(fig,ax, "2023-02-08T06:00:00.000000000")
    #plt.show()





