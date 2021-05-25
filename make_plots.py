def make_plots(subset_df, interp_df1, interp_df2, transect_number, var, min_var, max_var):
    '''
    Makes interpolation and raw data plots
    Input: Subset dataframe, interpolation grid, transect number, variable, minimum value, maximum values
    Output: Raw data figure, Interpolation figure
    '''
    from matplotlib import pyplot as plt
    plt.figure()
    plt.scatter(subset_df['distance'], subset_df['rangetobot'], c=subset_df[var], s = 3)
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Transect {:d} Original Data".format(transect_number))
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()

    plt.figure()
    plt.imshow(interp_df1.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.plot(subset_df['distance'], subset_df['rangetobot'], 'x', ms = 1, c = 'k')
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Transect {:d} Linear Interpolation".format(transect_number))
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")

    plt.figure()
    plt.imshow(interp_df2.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.plot(subset_df['distance'], subset_df['rangetobot'], 'x', ms = 1, c = 'k')
    plt.clim(min_var, max_var)
    if(var == 'oxygen'):
        plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    elif(var == 'temp'):
        plt.colorbar(label = "Temperature [\N{DEGREE SIGN}C]")
    elif(var == 'salinity'):
        plt.colorbar(label = "Salinity [PSU]")
    plt.title("Transect {:d} Cubic Spline Interpolation".format(transect_number))
    plt.xlabel("Transect Distance [m]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()

# generate a synthetic field with an exponential model
x = subset_df['distance']
y = subset_df['rangetobot']
model = gs.Exponential(dim=2, var=2, len_scale=8)
srf = gs.SRF(model, mean=0, seed=19970221)
field = srf((x, y))
# estimate the variogram of the field
bin_center, gamma = gs.vario_estimate((x, y), field)
# fit the variogram with a stable model. (no nugget fitted)
fit_model = gs.Stable(dim=2)
fit_model.fit_variogram(bin_center, gamma, nugget=False)
# output
ax = fit_model.plot(x_max=max(bin_center))
ax.scatter(bin_center, gamma)
print(fit_model)
