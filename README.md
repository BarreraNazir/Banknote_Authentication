# Banknote-Authentication-(UCI-Dataset)

Overview

Banknote authentication plays an important role for the central banks in order to keep the robustness of the financial system world wide, and keeping assurance in confidence documents, mostly banknotes. The whole process are divided in various parts, and then the results of classification are accomplish to achieve the final banknote authentication.

This task consist of three phases

1. Banknote Authentication Dataset:

    1.1 Dataset overview:
    
         Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
         
    1.2 Dataset details:
    
         The dataset contain 1372 rows and 5 variables namely, variance of Wavelet Transformed image (continuous),skewness of Wavelet Transformed image (continuous),curtosis of Wavelet Transformed image (continuous),entropy of image (continuous),class (integer). The dataset is known to have quality data where data don't have missing values nor outiers.
             
2. Pre-Processing:
    
         With the help of plots and summary statistics, outlier and missing values are not identified in the data. So, further moving to the next phase.
         
3. Classification:

        It predict numeric labels, to categorize banknotes as either authentic or forged. The classification include two steps:
        
        - Building the classifier or model:
        
            The classifier is build from the training set including the data of dependent and independent variable. 
            
        - Using classifier for classification:
        
            The classifier is used for classification. Here the test data is used to estimate the accuracy of models. The classifier can 
            be applied to new data if results is considered as acceptable. 
        
