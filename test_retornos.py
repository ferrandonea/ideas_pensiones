retornos = [
1,
2,
-1.5,
-0.5,
3.0,
0.2,
-0.1,
1.1,
1.3,
0.9
]

retornos_p = [1+round(r/100,4) for r in retornos]

import pandas as pd

df = pd.DataFrame(data=retornos_p)
df.columns = ["retornos_p"]

df["cumprod"] = df.cumprod()
df['cumprod_reverse'] = df.loc[::-1, 'retornos_p'].cumprod()[::-1]
df["cumprod_reverse_shift"] = df['cumprod_reverse'].shift(-1).fillna(1)

print (df)

#mujer
import numpy as np

def simula_retornos(mu_anual, sigma_anual, observaciones):
    mu = mu_anual/12
    sigma = sigma_anual/(np.sqrt(12))
    return np.random.normal(mu, sigma, observaciones)

fondob = simula_retornos(4.02/100, 8.53/100, (35-23)*12)
fondoc = simula_retornos(3.38/100, 6.19/100, (50-35)*12)
fondod = simula_retornos(2.81/100, 4.52/100, (60-50)*12)

print(fondob, fondoc, fondod)
print (type(fondob))

def merge_three(a,b,c):
    return np.append(np.append(a,b),c)

class Persona:
    def __init__(self) -> None:
        pass
    

def check_sex()