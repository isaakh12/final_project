def make_plots(subset_df, interp_df1, interp_df2, transect_number, var, min_var, max_var):
    '''
    Makes interpolation and raw data plots
    Input: Subset dataframe, interpolation grid, transect number, variable, minimum value, maximum values
    Output: Raw data figure, Interpolation figure
    '''
    from matplotlib import pyplot as plt
    grid = plt.GridSpec(2, 3, wspace=0, hspace=0) #set gridspace

    plt.figure(figsize = (18,8))
    plt.suptitle("Transect {:d}".format(transect_number), size = 20)
    plt.subplot(grid[0, 1])
    #graph raw data
    plt.scatter(subset_df['distance'], subset_df['rangetobot'], c=subset_df[var], s = 3)
    plt.clim(min_var, max_var)
    #set labels depending on variable used
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Original Data")
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")

    plt.subplot(grid[1, 0])
    #visualize interpolation (transposed so it appears correct)
    plt.imshow(interp_df1.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.plot(subset_df['distance'], subset_df['rangetobot'], 'x', ms = 1, c = 'k')
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Linear Interpolation")
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")


    plt.subplot(grid[1, 2])
    #visualize interpolation (transposed so it appears correct)
    plt.imshow(interp_df2.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.plot(subset_df['distance'], subset_df['rangetobot'], 'x', ms = 1, c = 'k')
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Cubic Spline Interpolation")
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()
