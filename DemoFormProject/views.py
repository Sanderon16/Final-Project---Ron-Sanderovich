"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from DemoFormProject import app
from DemoFormProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines


from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from DemoFormProject.Models.QueryFormStructure import QueryFormStructure 
from DemoFormProject.Models.QueryFormStructure import LoginFormStructure 
from DemoFormProject.Models.QueryFormStructure import UserRegistrationFormStructure 

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

### my functions:
from DemoFormProject.Models.DataQuery import plot_to_img
from DemoFormProject.Models.DataQuery import Get_NormalizedAverageWageDataset
from DemoFormProject.Models.DataQuery import Convert_StateCode_ToFullName
from DemoFormProject.Models.DataQuery import get_countries_choices

db_Functions = create_LocalDatabaseServiceRoutines() 

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='The application description page.'
    )


@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my picture album'
    )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    AverageWage_table = ''
    fig_image = ''
    df_avg =Get_NormalizedAverageWageDataset()

    form = QueryFormStructure(request.form)
     
    #set default values for time to avoid errors
    form.start_date.data = df_avg.TIME.min()
    form.end_date.data = df_avg.TIME.max()
    minmax = df_avg['TIME']

    #Set the list of states from the data set of al
    form.countries.choices = get_countries_choices()


    if (request.method == 'POST' ):
    
        ##query user parameters
        countries = ['AUS']
        start_date = form.start_date.data
        end_date = form.end_date.data
    #   kind = form.kind.data

        fig = plt.figure()
        
        for country in countries:
            #Filter only the requested countries
            df_avg_countries = df_avg.loc[ country ]
            # Filter only the requested Dates
            df_avg_dates = df_avg_countries.loc[lambda df: (df['TIME'] >= start_date) & (df['TIME'] <= end_date)]
            # create plot object ready for graphs
            plt.plot( 'TIME', 'Value', data=df_avg_dates, label = country)
            fig_image = plot_to_img(plt)
        
    return render_template('query.html', 
            form = form, 
            raw_data_table = AverageWage_table,
            fig_image = fig_image,
            title='User Data Query',
            year=datetime.now().year,
            message='Please enter the parameters you choose to analyze the database'
        )

# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def Register():
    form = UserRegistrationFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (not db_Functions.IsUserExist(form.username.data)):
            db_Functions.AddNewUser(form)
            db_table = ""

            flash('Thanks for registering new user - '+ form.FirstName.data + " " + form.LastName.data )
            # Here you should put what to do (or were to go) if registration was good
        else:
            flash('Error: User with this Username already exist ! - '+ form.username.data)
            form = UserRegistrationFormStructure(request.form)

    return render_template(
        'register.html', 
        form=form, 
        title='Register New User',
        year=datetime.now().year,
        repository_name='Pandas',
        )

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            return redirect('DataModel')
        else:
            flash('Incorrect username and/or password.')
   
    return render_template(
        'login.html',
        form=form, 
        title='Login Page',
        year=datetime.now().year,
        repository_name='Pandas',
        )



@app.route('/DataModel')
def DataModel():
    """Renders the data model page."""
    return render_template(
        'DataModel.html',
        title='Data Model',
        year=datetime.now().year,
        message='This is my Data Model page that covers the average salary across countries, with varying conditions'
        )




@app.route('/DataSet1')
def DataSet1():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\AverageWage.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the first data set page."""
    return render_template(
        'DataSet1.html',
        title='Average salaries',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page, youll be able to access a database containing the average salary of various countries through the years'
    )

@app.route('/DataSet2')
def DataSet2():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\WageGap.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the second data set page."""
    return render_template(
        'DataSet1.html',
        title='Average salaries',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='In this page, youll be able to access a database containing the wage gap between men and woman in various countries through the years'
    )


