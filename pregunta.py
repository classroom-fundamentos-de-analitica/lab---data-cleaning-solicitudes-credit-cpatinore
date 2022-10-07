"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd
import datetime as dt

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    #
    # Inserte su código aquí
    #

    df.sexo= df.sexo.str.lower().astype('category')
    df.tipo_de_emprendimiento= df.tipo_de_emprendimiento.str.lower().astype('category')
    df.estrato= df.estrato.astype('category')

    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio,infer_datetime_format=True,errors='coerce')
    df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime("%Y/%m/%d")

    df = df.dropna()
    df.drop_duplicates(inplace = True)
    

    return df
print(clean_data())