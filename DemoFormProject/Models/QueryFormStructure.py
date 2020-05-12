

#Quick note, QueryFormStructure is called like that because changing every single line of code where its mentioned is tedious.
#The actual name should be FormStructures.

### ----------------------------------------------------------- ###
### --- include all software packages and libraries needed ---- ###
### ----------------------------------------------------------- ###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
from os import path



from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import TextField, TextAreaField, SelectField, SelectMultipleField, DateField, DateTimeField
from wtforms import StringField, PasswordField, HiddenField, SubmitField
from wtforms import IntegerField, DecimalField, FloatField, RadioField, BooleanField

from wtforms import validators
from wtforms import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired

from wtforms.fields.html5 import DateField
### ----------------------------------------------------------- ###




## This class have the fields that are part of the Country-Capital demonstration
## You can see two fields:
##   the 'name' field - will be used to get the country name
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)

#def validdate(form, field):
#    if (field.data < 1990 or field.data > 2018):
#        raise ValidationError("must be between 1990 and 2018")

class QueryFormStructure(FlaskForm):
    countries = SelectMultipleField('Select Multiple:', validators = [DataRequired()])
    start_date = IntegerField('Start Date:' , validators = [DataRequired()])
    end_date  =  IntegerField('End Date:' , validators = [DataRequired()])
#    kind = SelectField('Chart Kind' , validators = [DataRequired] , choices=[('line'), ('bar')])
    submit = SubmitField('Submit')







## This class have the fields that are part of the Login form.
##   This form will get from the user a 'username' and a 'password' and sent to the server
##   to check if this user is authorised to continue
## You can see three fields:
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class LoginFormStructure(FlaskForm):
    username   = StringField('User name:  ' , validators = [DataRequired()])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')



## This class have the fields of a registration form
##   This form is where the user can register himself. It will have sll the information
##   we want to save on a user (general information) and the username ans PW the new user want to have
## You can see three fields:
##   the 'FirstName' field - will be used to get the first name of the user
##   the 'LastName' field - will be used to get the last name of the user
##   the 'PhoneNum' field - will be used to get the phone number of the user
##   the 'EmailAddr' field - will be used to get the E-Mail of the user
##   the 'username' field - will be used to get the username
##   the 'password' field - will be used to get the password
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
class UserRegistrationFormStructure(FlaskForm):
    FirstName  = StringField('First name:  ' , validators = [DataRequired()])
    LastName   = StringField('Last name:  ' , validators = [DataRequired()])
    PhoneNum   = StringField('Phone number:  ' , validators = [DataRequired()])     
    EmailAddr  = StringField('E-Mail:  ' , validators = [DataRequired('Email Address Required.')])
    username   = TextField('User name:  ' , validators = [DataRequired("please enter a password")])
    password   = PasswordField('Pass word:  ' , validators = [DataRequired()])
    submit = SubmitField('Submit')

## This class have the fields that the user can set, to have the query parameters for analysing the data
##   This form is where the user can set different parameters, depand on your project,
##   that will be used to do the data analysis (using Pandas etc.)
## You can see three fields:
##   The fields that will be part of this form are specific to your project
##   Please complete this class according to your needs
##   the 'submit' button - the button the user will press to have the 
##                         form be "posted" (sent to the server for process)
#class DataParametersFormStructure(FlaskForm):
#    
#    submit = SubmitField('Submit')


