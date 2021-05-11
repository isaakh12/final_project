def create_datasets(df, transect_number):
    import pandas as pd
    import numpy as np
    from scipy.interpolate import griddata
    from physoce import util
    transect = df[df['transect'] == transect_number]
    numpy_long = pd.Series.to_numpy(transect['longitude'])
    numpy_lat = pd.Series.to_numpy(transect['latitude'])
    numpy_dist = np.zeros([len(numpy_long), 1])
    haver = util.haversine(numpy_lat, numpy_long)
    numpy_dist[0] = 0.0
    for i in range(1,len(numpy_long)):
        numpy_dist[i] = numpy_dist[i-1] + haver[i-1]
    #transect.loc[:,'distance'] = numpy_dist
    transect['distance'] = numpy_dist
    grid_x, grid_y = np.mgrid[0:max(transect['distance']):1000j, 0:max(transect['rangetobot']):1000j]
    oxy_interp = griddata((transect['distance'], transect['rangetobot']), transect['oxygen'], (grid_x, grid_y), method='linear')
    min_oxy = min(df['oxygen'])
    max_oxy = max(df['oxygen'])
    return transect, oxy_interp, min_oxy, max_oxy
