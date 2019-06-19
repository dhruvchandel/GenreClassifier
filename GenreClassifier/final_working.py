def final_model(dic):
    from keras.models import load_model
    import numpy as np
    import os
    import pandas as pd
    
    df = pd.DataFrame(dic,index=[0])
    X_test = df.iloc[:,:].values
    current_path = os.getcwd()
    model_path = os.path.join(current_path, 'models')
    model = load_model(str(os.path.join(model_path, 'ANNmodel_4.h5py')))
    Y_pred = model.predict(X_test)
    
    print('\n\n here comes your result\n')
    print('action   --->%.2f'%(float(Y_pred[0][0])*100),'percent',sep = ' ')
    print('drama    --->%.2f'%(float(Y_pred[0][1])*100),'percent',sep = ' ')
    print('horror   --->%.2f'%(float(Y_pred[0][2])*100),'percent',sep = ' ')
    print('romance  --->%.2f'%(float(Y_pred[0][3])*100),'percent',sep = ' ')
   