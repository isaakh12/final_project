def mean_maker(subset_df, transect):
    import numpy as np
    oxy_means = []
    temp_means = []
    sal_means = []
    depth_means = []
    reef_means = []
    transect_list = []
    oxy_mean = np.mean(subset_df['oxygen'])
    temp_mean = np.mean(subset_df['temp'])
    sal_mean = np.mean(subset_df['salinity'])
    depth_mean = np.mean(subset_df['depth'])
    reef = str(np.unique(subset_df['reef']))
    oxy_means.append(oxy_mean)
    temp_means.append(temp_mean)
    sal_means.append(sal_mean)
    depth_means.append(depth_mean)
    reef_means.append(reef)
    transect_list.append(transect)
    return oxy_means, temp_means, sal_means, depth_means, reef_means, transect_list
