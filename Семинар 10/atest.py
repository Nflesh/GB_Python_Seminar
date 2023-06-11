import pandas as pd
import random
import numpy as np
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
data['human'] = np.where(data['whoAmI'] == 'human',1,0)
data['robot'] = np.where(data['whoAmI'] == 'robot',1,0)
data = data.drop(['whoAmI'],axis=1)