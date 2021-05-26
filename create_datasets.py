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
    pd.options.mode.chained_assignment = None #disregard warning message
    #make transect subset
    transect_sub = df[df['transect'] == transect_number]
    #translate latitude and longitude to numpy series
    numpy_long = pd.Series.to_numpy(transect_sub['longitude'])
    numpy_lat = pd.Series.to_numpy(transect_sub['latitude'])
    #initiate a numpy array for haversine distance
    numpy_dist = np.zeros([len(numpy_long), 1])
    #calculate haversine distances between each set of points
    haver = util.haversine(numpy_lat, numpy_long)
    numpy_dist[0] = 0.0
    #fill distance from transect start using current distance and haversine calculation
    for i in range(1,len(numpy_long)):
        numpy_dist[i] = numpy_dist[i-1] + haver[i-1]
    #convert km to m
    transect_sub['distance'] = numpy_dist*1000
    #set interpolation grids
    grid_x, grid_y = np.mgrid[0:max(transect_sub['distance']):1000j, 0:max(transect_sub['rangetobot']):1000j]
    #calculate interpolations
    interp_cubic = griddata((transect_sub['distance'], transect_sub['rangetobot']), transect_sub[var], (grid_x, grid_y), method='cubic')
    interp_linear = griddata((transect_sub['distance'], transect_sub['rangetobot']), transect_sub[var], (grid_x, grid_y), method='linear')
    #find minimum and maximum oxygen values
    min_var = min(df[var])
    max_var = max(df[var])
    return transect_sub, interp_linear, interp_cubic, min_var, max_var
