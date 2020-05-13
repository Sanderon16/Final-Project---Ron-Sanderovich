
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import base64
import datetime
import io
from os import path

# -------------------------------------------------------------------------------
# Function to convert a plot to an image that can be integrated into an HTML page       
# -------------------------------------------------------------------------------
def plot_to_img(fig):
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

# -------------------------------------------------------
# Function that get a dataset that include in the columns 
# -------------------------------------------------------
def Get_NormalizedAverageWageDataset():
    dfw = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\Data\\AverageWage.csv"))
    # Keep only the columns I will need
    dff = dfw.drop(['INDICATOR','SUBJECT','MEASURE','FREQUENCY',"Flag Codes"], axis = 1)
    dff = dff.set_index(['LOCATION'])
    return (dff)
#----------------------------------------------------------------
#Function that replaces 3 letter country names by their full name
#----------------------------------------------------------------
def Convert_StateCode_ToFullName(df): #doesnt work for some reason i spent 3 hours trying to figure out
    df_short_state = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\Data\\countries_codes_and_coordinates.csv"))
    s = df_short_state.set_index('Alpha-3 code')['Country']
    return (pd.merge(df, s, how='outer', on=['LOCATION', 'Country']))

#-------------------------------
#generates list of all countries
#-------------------------------
def get_countries_choices():
    df_short_state = pd.read_csv(path.join(path.dirname(__file__), "..\\static\\Data\\AverageWage.csv"))
    df1 = df_short_state.groupby('LOCATION').sum()
    l = df1.index
    m = list(zip(l , l))
    return m



