def funcion_1(archivo):
    import pandas as pd
    import os

    extension=os.path.splitext(archivo)[1].lower()
    if extension == ".csv":
        df = pd.read_csv(archivo)
        df = df.drop(columns="Unnamed: 0", errors="ignore")
        return(df)
    elif extension == ".html":
        df = pd.read_html(archivo)
        df = df.drop(columns="Unnamed: 0", errors="ignore")
        return(df)
    elif extension == ".xlsx":
        df = pd.read_excel(archivo)
        df = df.drop(columns="Unnamed: 0", errors="ignore")
        return(df)
    else:
        raise ValueError (f"“Hola, acabas de ingresar un documento que desconozco, con extensión: {archivo}")

def funcion_2(df):
    import pandas as pd
    import os
    primos = [col for i, col in enumerate(df.columns) if i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 869, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]]

    for col in df.columns:
        if col in primos:
            df[col].fillna(1111111, inplace=True)
        elif df[col].dtype in ['int64', 'float64',"int","float"]:
            df[col].fillna(1000001, inplace=True)
        else:
            df[col] = df[col].fillna("Valor Nulo")
    
    return(df)
    
def funcion_3(df):
    import pandas as pd
    import os

    valores_nulos=df.isnull().sum()
    print("""Por Columna:
          """,valores_nulos)
    valores_nulos2=df.isnull().sum().sum()
    print("""Por DataFrame:
          """,valores_nulos2)
    
def funcion_4(df):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    cuantitativas=df.select_dtypes(include=["float64","int64","float","int"])
    cualitativas=df.select_dtypes(include=["object","datetime","category"])
    y=cuantitativas

    percentile25=y.quantile(0.25)
    percentile75=y.quantile(0.75)
    iqr= percentile75-percentile25

    Limite_Superior_iqr= percentile75+1.5*iqr
    Limite_Inferior_iqr= percentile25-1.5*iqr
    iqr=cuantitativas[(y<=Limite_Superior_iqr)&y>=(Limite_Inferior_iqr)]
    iqr2=iqr.fillna(round(iqr.mean(),1))
    iqr3=pd.concat([cualitativas,iqr2],axis=1)
    return(iqr3)