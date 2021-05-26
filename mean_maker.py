def mean_maker(subset_df, transect, oxy_means, temp_means, sal_means, depth_means, reef_means, transect_list):
    '''
    Function that makes lists of means for each variable
    Input: subset dataframe, transect number, empty lists of variables that you want to average
    Output: Filled list of variables and transect number
    '''
    import numpy as np
    #calculate mean of each variable
    oxy_mean = np.mean(subset_df['oxygen'])
    temp_mean = np.mean(subset_df['temp'])
    sal_mean = np.mean(subset_df['salinity'])
    depth_mean = np.mean(subset_df['depth'])
    #find out which reef condition this transect has
    reef = str(np.unique(subset_df['reef']))
    #add means to end of lists input into function
    oxy_means.append(oxy_mean)
    temp_means.append(temp_mean)
    sal_means.append(sal_mean)
    depth_means.append(depth_mean)
    reef_means.append(reef)
    transect_list.append(transect)
    return oxy_means, temp_means, sal_means, depth_means, reef_means, transect_list
