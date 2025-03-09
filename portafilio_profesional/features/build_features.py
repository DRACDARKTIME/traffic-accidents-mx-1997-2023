import pandas as pd

def top_5(colum=None,df=None, tc=None,tc_name=None, tc_option=False, top=5):
    colum_total = df[colum].value_counts()
    top_5_colum = colum_total.head(top).index
    if tc_option:
        etiquetas_x = tc[tc[colum].isin(top_5_colum)][tc_name]
        etiquetas_x = etiquetas_x.tolist()
    else:
        etiquetas_x = []
    df_top_5 = df[df[colum].isin(top_5_colum)]
    return df_top_5, etiquetas_x