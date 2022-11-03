import pandas as pd

mortality_table = "/Users/franciscoerrandonea/Library/CloudStorage/OneDrive-FocusAGF/Repos/pensiones/tablasmortalidad2020.xlsx"
sheets = ["RV-2020, Mujeres", "CB-2020, Hombres"]

def read_mortality_sheet(mortality_table: str, sheet: str) -> pd.DataFrame:
    columns = ["qx"] + [year for year in range(2016,2037)]
    return pd.read_excel(mortality_table, sheet_name=sheets[0], header = None, index_col=0, skiprows=range(8), skipfooter=5, names = columns)
    

df = dict()
mortalidad = dict()
mejoramiento = dict()
for sheet in sheets:
    df = read_mortality_sheet(mortality_table, sheet)
    mejoramiento[sheet] = df.iloc[:,1:]
    mortalidad[sheet] = df.iloc[:,0]
