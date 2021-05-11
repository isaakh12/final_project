def make_plots(subset_df, oxy_df, transect_number, min_oxy, max_oxy):
    from matplotlib import pyplot as plt
    plt.figure()
    plt.scatter(subset_df['distance'], subset_df['rangetobot'], c=subset_df['oxygen'])
    plt.clim(min_oxy, max_oxy)
    plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    plt.title("Transect {:d} Original Data".format(transect_number))
    plt.xlabel("Transect Distance [km]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()

    plt.figure()
    plt.imshow(oxy_df.T, extent=(0,max(subset_df['distance']),0,max(subset_df['rangetobot'])), origin='lower', aspect = 'auto', cmap='viridis')
    plt.clim(min_oxy, max_oxy)
    plt.colorbar(label = "Oxygen [\u03BCmol/L]")
    plt.title("Transect {:d} Interpolation".format(transect_number))
    plt.xlabel("Transect Distance [km]")
    plt.ylabel("Depth above seafloor [m]")
    plt.show()
