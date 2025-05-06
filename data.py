import pandas as pd

file = r'C:\Users\KethylleRaianeCurySe\OneDrive - Math Group\Área de Trabalho\DataProjects\DataScience\conceito_enade_2023.xlsx'
file_saida = r'C:\Users\KethylleRaianeCurySe\OneDrive - Math Group\Área de Trabalho\DataProjects\DataScience\conceito_enade_tratado.xlsx'

def ler_arquivo(file):

    df = pd.read_excel(file)
    print(df.info())
    print(df.describe())
    return df

def tratar_dados(df):
  
    print(df.isnull().sum())
    df['Conceito Enade (Faixa)'] = df['Conceito Enade (Faixa)'].replace('SC', pd.NA)
    df['Sigla da IES*'] = df['Sigla da IES*'].fillna('Desconhecida')
    df['Conceito Enade (Contínuo)'] = df['Conceito Enade (Contínuo)'].fillna(0)
    df['Nota Bruta - FG'] = df['Nota Bruta - FG'].fillna(0)
    df['Nota Padronizada - FG'] = df['Nota Padronizada - FG'].fillna(0)
    df['Nota Bruta - CE'] = df['Nota Bruta - CE'].fillna(0)
    df['Nota Padronizada - CE'] = df['Nota Padronizada - CE'].fillna(0)
    df = df[pd.to_numeric(df['Ano'], errors='coerce').notna()]

    print(df.isnull().sum())
    return df

def selecionar_atributos_relevantes(df):
    df_relevante = df[['Ano', 'Código da Área', 'Área de Avaliação', 'Grau Acadêmico', 'Modalidade de Ensino',
                       'Código da IES', 'Nome da IES*', 'Sigla da IES*', 'Categoria Administrativa', 'Organização Acadêmica',
                       'Código do Município**', 'Município do Curso**', 'Sigla da UF** ', 'Nº de Concluintes Inscritos',
                       'Nº  de Concluintes Participantes', 'Nota Bruta - FG', 'Nota Padronizada - FG',
                       'Nota Bruta - CE', 'Nota Padronizada - CE', 'Conceito Enade (Contínuo)', 'Conceito Enade (Faixa)']]
    return df_relevante

def media_conceito_por_area(df): 
    agg_conceito= df.groupby('Área de Avaliação')['Conceito Enade (Contínuo)'].mean()
    return agg_conceito

def salvar_arquivo(df_relevante, file_saida): 
    df_relevante.to_excel(file_saida, index=False)
    


df = ler_arquivo(file)
df_tratado = tratar_dados(df)
df_relevante = selecionar_atributos_relevantes(df_tratado)
agg_conceito = media_conceito_por_area(df_relevante)
salvar_arquivo(df_tratado, file_saida)
