import math
import numpy as np
from datetime import date
import pandas as pd

def check_gender(gender):
    gender = gender.upper()
    # Masculino = M
    # Femenino = F
    # No existe opcion distinta x regulacion
    
    if gender not in ["M","F"]:
        raise ValueError("Gender debe ser --> F: Femenino, M: Masculino")
    return gender

def fondo_recomendado(age:int, gender:str):
    gender = check_gender(gender)
    
    if age < 35:
        return "B"
    
    if gender == "F":
        if age >=50:
            return "D"
        return "C"

    if gender == "M":
        if age >=55:
            return "D"
        return "C"



class Fondo:
    def __init__(self, mu, sigma, nombre) -> None:
        #mu y sigma en base anual y en puntos base
        # es decir 4.49 es 4.49/100
        self.mu = mu /100
        self.sigma = sigma /100        
        self.nombre = nombre # nombre del fondo
        
        self.mu_mensual = self.mu/12
        self.sigma_mensual = self.sigma/math.sqrt(12)

        
    def __repr__(self) -> str:
        return f"Fondo {self.nombre} -> [ mu = {self.mu:.2%}, sigma= {self.sigma:.2%} ]"

fondos = {
    "A": Fondo(4.49, 10.99, "A"),
    "B": Fondo(4.02, 8.53, "B"),
    "C": Fondo(3.38, 6.19, "C"),
    "D": Fondo(2.81, 4.52, "D"),
    "E": Fondo(2.17, 4.12, "E"),
    "RV": Fondo(3.11, 0.65, "RV"),    
    }



class Persona:
    def __init__(self, gender: str, retirement_age = None, years_at_first_job: int = 23) -> None:
        self.gender = check_gender(gender)
        if retirement_age:
            self.retirment_age = retirement_age
        else:
            self.retirment_age = 60
            if self.gender == "M":
                self.retirment_age = 65
        self.months_working = (self.retirment_age - years_at_first_job)*12
        #print (self.months_working)
        
        lst_months = []
        for working_month in range(1,self.months_working+1):
            age  = int((working_month-1)/12)+years_at_first_job
            fund = fondo_recomendado(age, self.gender)
            
            monthly_mu = fondos[fund].mu_mensual
            monthly_sigma = fondos[fund].sigma_mensual            
            fund_return = 1 + np.random.normal(monthly_mu, monthly_sigma)
            lst_months.append(fund_return)
        self.returns_history = np.array(lst_months)
        self.cum_returns = self.returns_history.prod()
        
            
            
            
hola = Persona("F", years_at_first_job=24)                
        
df = hola.returns_history

def mean_list(lst):
    return sum(lst)/len(lst)

import time
start = time.perf_counter()
promedio = 0.01
lst_simula = []
for simulation in range(100_000):    
    hola = Persona("F", years_at_first_job=24)                
    lst_simula.append(hola.cum_returns)
    # if abs(mean_list(lst_simula)/promedio-1) < 0.0000001:
    #     print (simulation)
    #     break
promedio = mean_list(lst_simula)
print (promedio)    
print (time.perf_counter() - start)
    
    
    
    
    


def calculate_age(born: date, today: date = date.today()):
    #pirateado de https://stackoverflow.com/questions/2217488/age-from-birthdate-in-python
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



def elige_fondo_random(age:int, gender:str):
    gender = check_gender(gender)
    # elije un fondo al achunte, pero con las restricciones de edad
    multifondos = list("ABCDE")
    if ( gender == "F" and age >=51 ) or ( gender == "M" and age >=56 ):
        multifondos.remove("A")
    return np.random.choice(multifondos)
    
    



#mujeres 
# 0-35 B
# 35-50 C
# D

#hombres
# 0-35 B
# 0-55 C
# 56 D