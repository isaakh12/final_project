def make_pca(df, vars):
    '''
    Function used to conduct a PCA
    Input: dataframe, list of variables that you want to use in your PCA
    Output: Eigenvalues, Eigenvectors, Proportion of variance taken up by first 2 PCs, Factor Loadings
    '''
    import numpy as np
    from scipy import linalg
    from matplotlib import pyplot as plt
    data = df[vars]
    data_norm = np.zeros([len(data),len(vars)]) #make an empty data matrix
    means = np.mean(data, axis=0) #compute the means of the variables
    stds = np.std(data, axis = 0, ddof=1) #compute the standard deviations of the variables
    data_norm = (data - means) / stds #standardize the data across all variables so it can be compared

    #create covariance matrix
    R = np.cov(data_norm, rowvar=False)

    #extract eigenvalues and eigenvectors
    eig_val, eig_vec = linalg.eig(R) #compute eigenvalues and eigenvectors
    eig_val = np.real(eig_val) #assign the eigenvalues to be real numbers (take away the j bit)
    print("Eigenvalues:", eig_val)
    print("Eigenvectors: \n", eig_vec)


    sorted_indices = np.argsort(eig_val)[::-1] #find the sorted indices using the argsort function
    eig_val = eig_val[sorted_indices] #reassign the eigenvalues to their sorted indices
    eig_vec = eig_vec[:,sorted_indices] #reassign the eigenvectors to their sorted indices but keep the columns intact

    tot = np.sum(eig_val) #sum all the eigenvalues to compute the total variance
    PC1 = eig_val[0] #assign a variable to be the variance of PC1
    PC2 = eig_val[1] #assign a variable to be the variance of PC2
    PC1_prop = (PC1/tot) * 100 #compute percentage of variance acccounted for by PC1
    PC2_prop = (PC2/tot) * 100 #compute percentage of variance acccounted for by PC2
    print("Variance accounted for by PC1:", PC1_prop, "%")
    print("Variance accounted for by PC2:", PC2_prop, "%")

    eig_val_zeros = np.diag(eig_val) #make a new matrix of the eigenvalues with 0's in the right spots
    A = np.matmul(eig_vec, eig_val_zeros**0.5) #multiply the eigenvector matrix by the eigenvalue matrix

    plt.figure()
    plt.xlabel('PC1 loading')
    plt.ylabel('PC2 loading')
    variables = ['temperature', 'salinity', 'oxygen'] #make a variable of a list of the response variables
    for i,txt in enumerate(variables): #loop through the list of response variables
        plt.plot([0,A[i,0]],[0,A[i,1]],'.-', label = txt, ms=10) #plot each variable's factor loading
        plt.plot(0,0,'.', ms=10, c='k') #add a black dot at (0,0)
        plt.legend(loc='lower left') #add a legend
        plt.title("Factor Loadings")
