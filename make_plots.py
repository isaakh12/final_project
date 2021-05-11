def make_plots(subset_df, interp_df, transect_number, var, min_var, max_var):
    '''
    Makes interpolation and raw data plots
    Input: Subset dataframe, interpolation grid, transect number, variable, minimum value, maximum values
    Output: Raw data figure, Interpolation figure
    '''
    from matplotlib import pyplot as plt
    plt.figure()
    plt.scatter(subset_df['distance'], subset_df['rangetobot'], c=subset_df[var])
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Transect {:d} Original Data".format(transect_number))
    plt.xlabel("Transect Distance [km]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()

    plt.figure()
    plt.imshow(interp_df.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Transect {:d} Interpolation".format(transect_number))
    plt.xlabel("Transect Distance [km]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()
