def create_datasets(df, transect_number, var):
    '''
    Used to prepare datasets for visualization
    Takes a subset for each transect number (if used within for loop)
    Takes lat/long data and translates into transect distance
    Takes distance and an interpolated variable and outputs a grid of interpolated data
    Input: dataframe with latitude, longitude, transect, range to bottom, and some response variable
    Output: subset of data, interpolation grid, minimum value, maximum value
    '''
    import pandas as pd
    import numpy as np
    from scipy.interpolate import griddata
    from physoce import util
    transect_sub = df[df['transect'] == transect_number]
    numpy_long = pd.Series.to_numpy(transect_sub['longitude'])
    numpy_lat = pd.Series.to_numpy(transect_sub['latitude'])
    numpy_dist = np.zeros([len(numpy_long), 1])
    haver = util.haversine(numpy_lat, numpy_long)
    numpy_dist[0] = 0.0
    for i in range(1,len(numpy_long)):
        numpy_dist[i] = numpy_dist[i-1] + haver[i-1]
    transect_sub['distance'] = numpy_dist
    grid_x, grid_y = np.mgrid[0:max(transect_sub['distance']):1000j, 0:max(transect_sub['rangetobot']):1000j]
    interp = griddata((transect_sub['distance'], transect_sub['rangetobot']), transect_sub[var], (grid_x, grid_y), method='linear')
    min_var = min(df[var])
    max_var = max(df[var])
    return transect_sub, interp, min_var, max_var
