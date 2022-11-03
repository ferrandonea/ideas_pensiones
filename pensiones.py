import numpy as np

def is_femenine(gender_str:str) -> bool:
    # if Female returns True
    # if masculine returns False
    # otherwise fails 
    if gender_str.upper() not in ["F","M"]:
        raise ValueError("Sex should be either M (Male) or F (Female)")
    return gender_str.upper() == "F"

def simulate_monthly_returns(mu_annual : float, sigma_annual: float, observations: int) -> np.ndarray:
    mu = mu_annual / 12
    sigma = sigma_annual / (np.sqrt(12))
    return np.random.normal(mu, sigma, observations)

def string_to_float(number_str:str, precision:int=5):
    #aux function to simplify reading fund assumptions
    return round(float(number_str)/100,precision)

def read_funds_assumptions():
    with open("fundshistory.csv", "r") as f:
        datos = f.readlines()
        data = {}
        for x in datos: 
            x = x.strip().split(";")
            data.update({x[0]:{"mu":string_to_float(x[1]),"sigma":string_to_float(x[2])}})
    return data    

class Fund:
    def __init__(self) -> None:
        #opens file with assumptions
        pass

            


class Human:
    def __init__(self, gender_str:str, first_job:int=23, retirement_age:int=None) -> None:
        '''
        gender_str: gender M:Masculine, F:Femenine
        first_job= Age at first job
        retirment age = self explanatory
        '''
        self.gender = is_femenine(gender_str) # femenine = True, masculine=False
        self.first_job = first_job
        
        if not retirement_age:
            self.retirment_age = 65
            if self.gender:                
                self.retirment_age = 60
        else:
            self.retirment_age = retirement_age
            
        self.working_years = self.retirment_age - self.first_job
    
        if self.gender:
            #femenine
            fondob = simula_retornos(4.02/100, 8.53/100, (35-23)*12)
            fondoc = simula_retornos(3.38/100, 6.19/100, (50-35)*12)
            fondod = simula_retornos(2.81/100, 4.52/100, (60-50)*12)


    