#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[4]:


black_friday.columns


# In[5]:


df = black_friday


# In[6]:


df.head(5)


# In[15]:


df.shape


# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[17]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return df.shape 
q1()


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[18]:


def q2():
    # Retorne aqui o resultado da questão 2.
    # return df[(df['Age'] == '26-35') & (df['Gender'] == 'F')].shape[0]
    return df.query("Gender == 'F' & Age == '26-35'").shape[0]
q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[19]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return df['User_ID'].nunique()
q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[20]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return df.dtypes.nunique()
q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[21]:


def q5():
    # Retorne aqui o resultado da questão 5.
    
    # Total lines
    tot = df.shape[0]
    
    # Total lines without null value
    non_null = df.dropna().shape[0]
    
    # Lines with some null value: Total lines - Lines with Null
    null_lines = tot - non_null
    
    return null_lines / tot

q5()
    


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[23]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return int(df.isnull().sum().max())
q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[24]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return df['Product_Category_3'].mode().values[0]
q7()


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[27]:


def q8():
    # Retorne aqui o resultado da questão 8.
    # Select Purchase columns
    purch = df['Purchase']
    # Get normalized values
    norm = (purch - purch.min()) / (purch.max() - purch.min())
    return float(norm.mean())
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[28]:


def q9():
    # Retorne aqui o resultado da questão 9.
    # Select Purchase columns
    purch = df['Purchase']
    # Get padronized values
    padr = (purch - purch.mean()) / (purch.std())
    return padr[(padr < 1) & (padr > -1)].shape[0]
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[29]:


def q10():
    # Retorne aqui o resultado da questão 10.
    # Select Null values from Product_Category_2
    null_cat_two = df[df['Product_Category_2'].isnull()]
    # Return min from is null on  Product_Category_3 if there is a null value the result is False
    return bool(null_cat_two['Product_Category_3'].isnull().min())
q10()


# In[ ]:




