# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Process
            ### Data Wrangling
            The dataset used is the same as in my previous build project 
            (which can be viewed at https://raymond98tan.github.io/2020-08-27-Build-Project01/)
            The data collected was scraped off my own playlists using
            http://organizeyourmusic.playlistmachinery.com/.
            
            Because the data didn't have many NaN values, the cleaning process
            was relatively easy. However, there were columns in the dataset with
            high cardinality, namely top genre, artist, and title. There were
            also useless columns such as year, added, and dur which needed to be
            removed from the dataset. Lastly, I feature engineered the target variable
            using the valence variable(positive). From my last build project, I discovered that
            the songs which were grouped in the the 2 most energetic playlist groups
            had valences of > 60. Therefore, I decided to define songs with a valence
            of >= 60 to be positive. After engineering this feature, I removed the
            valence variable to prevent the leakage.

            ### Splitting the data
            Once the data was wrangled, I used a random split to split the data into
            training, validation, and testing sets. 

            ### Baseline
            After splitting the datasets, I used the training set to set a baseline
            for the models I will make. The baseline turned out that 76% of the data
            was not positive, meaning that if we were to assume a song was not positive, 
            that assumption would be correct 76% of the time.

            ### Building the Model
            Once the baseline was set, I then created three separate models to see which 
            would best model the data. I first created a logistic regression model. I then 
            created a random forest classifier. Lastly, I created a XGBoost classifier.
            Of these three models, the Random Forest Classifier had the best validation
            accuracy of 0.79, 0.03% greater than the baseline.
            """
        ),

    ],
)

layout = dbc.Row([column1])