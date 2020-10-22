# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app

pipeline = load('assets/pipeline.joblib')

@app.callback(Output('prediction-content', 'children'),
                [Input('name', 'value'),
                 Input('category', 'value'),
                 Input('main_category', 'value'),
                 Input('currency', 'value'),
                 Input('state', 'value'),
                 Input('usd_goal_real', 'value'),
                 Input('length_days', 'value')])

def predict(name, category, main_category, currency, state, usd_goal_real, length_days):
    df = pd.DataFrame(
        columns = ['name', 'category', 'main_category', 'currency', 'state', 'usd_goal_real', 'length_days'],
        data = [[name, category, main_category, currency, state, usd_goal_real, length_days]]
    )
    
    y_pred = pipeline.predict(df)[0]

    print(df)
    print(y_pred)
    
    return f'Succeed? {y_pred}'

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Name'), 
        dcc.Slider(
            id='name', 
            min=1, 
            max=27, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(1,27,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Category'), 
        dcc.Dropdown(
            id='category', 
            options = [
                {'label': 'Product Design', 'value': 'Product Design'},
                {'label': 'Documentary', 'value': 'Documentary'},
                {'label': 'Music', 'value': 'Music'},
                {'label': 'Tabletop Games', 'value': 'Tabletop Games'},
                {'label': 'Shorts', 'value': 'Shorts'},
                {'label': 'Video Games', 'value': 'Video Games'},
                {'label': 'Food', 'value': 'Food'},
                {'label': 'Film & Video', 'value': 'Film & Video'},
                {'label': 'Fiction', 'value': 'Fiction'},
                {'label': 'Fashion', 'value': 'Fashion'},
                {'label': 'Nonfiction', 'value': 'Nonfiction'},
                {'label': 'Art', 'value': 'Art'},
                {'label': 'Apparel', 'value': 'Apparel'},
                {'label': 'Theater', 'value': 'Theater'},
                {'label': 'Technology', 'value': 'Technology'},
                {'label': 'Rock', 'value': 'Rock'},
                {'label': "Children's Books", 'value': "Children's Books"},
                {'label': 'Apps', 'value': 'Apps'},
                {'label': 'Publishing', 'value': 'Publishing'} ,
                {'label': 'Webseries', 'value': 'Webseries'},
                {'label': 'Photography', 'value': 'Photography'},
                {'label': 'Indie Rock', 'value': 'Indie Rock'},
                {'label': 'Narrative Film', 'value': 'Narrative Film'},
                {'label': 'Web', 'value': 'Web'},
                {'label': 'Comics', 'value': 'Comics'},
                {'label': 'Crafts', 'value': 'Crafts'} ,
                {'label': 'Country & Folk', 'value': 'Country & Folk'},
                {'label': 'Design', 'value': 'Design'},
                {'label': 'Hip-Hop', 'value': 'Hip-Hop'},
                {'label': 'Hardware', 'value': 'Hardware'},
                {'label': 'Pop', 'value': 'Pop'},
                {'label': 'Painting', 'value': 'Painting'},
                {'label': 'Games', 'value': 'Games'},
                {'label': 'Illustration', 'value': 'Illustration'},
                {'label': 'Accessories', 'value': 'Accessories'},
                {'label': 'Public Art', 'value': 'Public Art'},
                {'label': 'Software', 'value': 'Software'},
                {'label': 'Gadgets', 'value': 'Gadgets'},
                {'label': 'Restaurants', 'value': 'Restaurants'},
                {'label': 'Mixed Media', 'value': 'Mixed Media'},
                {'label': 'Comic Books', 'value': 'Comic Books'},
                {'label': 'Art Books', 'value': 'Art Books'},
                {'label': 'Classical Music', 'value': 'Classical Music'},
                {'label': 'Animation', 'value': 'Animation'},
                {'label': 'Playing Cards', 'value': 'Playing Cards'},
                {'label': 'Drinks', 'value': 'Drinks'},
                {'label': 'Dance', 'value': 'Dance'},
                {'label': 'Comedy', 'value': 'Comedy'},
                {'label': 'Drama', 'value': 'Drama'},
                {'label': 'Electronic Music', 'value': 'Electronic Music'},
                {'label': 'Performance Art', 'value': 'Performance Art'},
                {'label': 'World Music', 'value': 'World Music'},
                {'label': 'Graphic Design', 'value': 'Graphic Design'},
                {'label': 'Graphic Novels', 'value': 'Graphic Novels'},
                {'label': 'Jazz', 'value': 'Jazz'},
                {'label': 'Sculpture', 'value': 'Sculpture'},
                {'label': 'Small Batch', 'value': 'Small Batch'},
                {'label': 'Mobile Games', 'value': 'Mobile Games'},
                {'label': 'Food Trucks', 'value': 'Food Trucks'},
                {'label': 'Journalism', 'value': 'Journalism'},
                {'label': 'Photobooks', 'value': 'Photobooks'},
                {'label': 'Plays', 'value': 'Plays'},
                {'label': 'Poetry', 'value': 'Poetry'},
                {'label': 'Digital Art', 'value': 'Digital Art'},
                {'label': 'Horror', 'value': 'Horror'},
                {'label': 'Periodicals', 'value': 'Periodicals'},
                {'label': 'Jewelry', 'value': 'Jewelry'},
                {'label': 'Wearables', 'value': 'Wearables'},
                {'label': 'DIY', 'value': 'DIY'},
                {'label': 'Woodworking', 'value': 'Woodworking'},
                {'label': 'Farms', 'value': 'Farms'},
                {'label': 'People', 'value': 'People'},
                {'label': 'Faith', 'value': 'Faith'},
                {'label': 'Live Games', 'value': 'Live Games'},
                {'label': 'Conceptual Art', 'value': 'Conceptual Art'},
                {'label': 'Television', 'value': 'Television'},
                {'label': 'Performances', 'value': 'Performances'},
                {'label': 'Footwear', 'value': 'Footwear'},
                {'label': 'Experimental', 'value': 'Experimental'},
                {'label': 'Radio & Podcasts', 'value': 'Radio & Podcasts'},
                {'label': 'Academic', 'value': 'Academic'},
                {'label': 'Musical', 'value': 'Musical'},
                {'label': 'DIY Electronics', 'value': 'DIY Electronics'},
                {'label': 'Ready-to-wear', 'value': 'Ready-to-wear'},
                {'label': 'Spaces', 'value': 'Spaces'},
                {'label': 'Festivals', 'value': 'Festivals'},
                {'label': 'Young Adult', 'value': 'Young Adult'},
                {'label': 'Events', 'value': 'Events'},
                {'label': 'Anthologies', 'value': 'Anthologies'},
                {'label': 'Fine Art', 'value': 'Fine Art'},
                {'label': 'Architecture', 'value': 'Architecture'},
                {'label': 'Thrillers', 'value': 'Thrillers'},
                {'label': 'Science Fiction', 'value': 'Science Fiction'},
                {'label': 'Action', 'value': 'Action'},
                {'label': 'Places', 'value': 'Places'},
                {'label': 'Print', 'value': 'Print'},
                {'label': 'Metal', 'value': 'Metal'},
                {'label': 'Music Videos', 'value': 'Music Videos'},
                {'label': '3D Printing', 'value': '3D Printing'},
                {'label': 'Sound', 'value': 'Sound'},
                {'label': 'Webcomics', 'value': 'Webcomics'},
                {'label': 'Vegan', 'value': 'Vegan'},
                {'label': 'Nature', 'value': 'Nature'},
                {'label': 'Robots', 'value': 'Robots'},
                {'label': 'Cookbooks', 'value': 'Cookbooks'},
                {'label': 'Childrenswear', 'value': 'Childrenswear'},
                {'label': 'Installations', 'value': 'Installations'},
                {'label': 'R&B', 'value': 'R&B'},
                {'label': 'Candles', 'value': 'Candles'},
                {'label': 'Video', 'value': 'Video'},
                {'label': 'Gaming Hardware', 'value': 'Gaming Hardware'},
                {'label': 'Flight', 'value': 'Flight'},
                {'label': "Farmer's Markets", 'value': "Farmer's Markets"},
                {'label': 'Camera Equipment', 'value': 'Camera Equipment'},
                {'label': 'Audio', 'value': 'Audio'},
                {'label': 'Interactive Design', 'value': 'Interactive Design'},
                {'label': 'Zines', 'value': 'Zines'},
                {'label': 'Fantasy', 'value': 'Fantasy'},
                {'label': 'Family', 'value': 'Family'},
                {'label': 'Immersive', 'value': 'Immersive'},
                {'label': 'Calendars', 'value': 'Calendars'},
                {'label': 'Space Exploration', 'value': 'Space Exploration'},
                {'label': 'Punk', 'value': 'Punk'},
                {'label': 'Ceramics', 'value': 'Ceramics'},
                {'label': 'Community Gardens', 'value': 'Community Gardens'},
                {'label': 'Civic Design', 'value': 'Civic Design'},
                {'label': 'Kids', 'value': 'Kids'},
                {'label': 'Literary Journals', 'value': 'Literary Journals'},
                {'label': 'Textiles', 'value': 'Textiles'},
                {'label': 'Couture', 'value': 'Couture'},
                {'label': 'Blues', 'value': 'Blues'},
                {'label': 'Animals', 'value': 'Animals'},
                {'label': 'Fabrication Tools', 'value': 'Fabrication Tools'},
                {'label': 'Printing', 'value': 'Printing'},
                {'label': 'Makerspaces', 'value': 'Makerspaces'},
                {'label': 'Movie Theaters', 'value': 'Movie Theaters'},
                {'label': 'Puzzles', 'value': 'Puzzles'},
                {'label': 'Bacon', 'value': 'Bacon'},
                {'label': 'Stationery', 'value': 'Stationery'},
                {'label': 'Photo', 'value': 'Photo'},
                {'label': 'Video Art', 'value': 'Video Art'},
                {'label': 'Romance', 'value': 'Romance'},
                {'label': 'Knitting', 'value': 'Knitting'},
                {'label': 'Workshops', 'value': 'Workshops'},
                {'label': 'Crochet', 'value': 'Crochet'},
                {'label': 'Translations', 'value': 'Translations'},
                {'label': 'Pet Fashion', 'value': 'Pet Fashion'},
                {'label': 'Glass', 'value': 'Glass'},
                {'label': 'Latin', 'value': 'Latin'},
                {'label': 'Embroidery', 'value': 'Embroidery'},
                {'label': 'Typography', 'value': 'Typography'},
                {'label': 'Pottery', 'value': 'Pottery'},
                {'label': 'Weaving', 'value': 'Weaving'},
                {'label': 'Quilts', 'value': 'Quilts'},
                {'label': 'Residencies', 'value': 'Residencies'},
                {'label': 'Letterpress', 'value': 'Letterpress'},
                {'label': 'Chiptune', 'value': 'Chiptune'},
                {'label':  'Literary Spaces', 'value': 'Literary Spaces'},
                {'label': 'Taxidermy', 'value': 'Taxidermy'}
            ], 
            value = 'Taxidermy', 
            className='mb-5', 
        ),
        dcc.Markdown('#### Main Category'),
        dcc.Dropdown(
            id='main_category', 
            options = [
                {'label': 'Film & Video', 'value': 'Film & Video'}, 
                {'label': 'Music', 'value': 'Music'}, 
                {'label': 'Publishing', 'value': 'Publishing'}, 
                {'label': 'Games', 'value': 'Games'}, 
                {'label': 'Techonology', 'value': 'Technology'}, 
                {'label': 'Art', 'value': 'Art'},
                {'label': 'Food', 'value': 'Food'},
                {'label': 'Fashion', 'value': 'Fashion'},
                {'label': 'Theater', 'value': 'Theater'},
                {'label': 'Comics', 'value': 'Comics'},
                {'label': 'Photography', 'value': 'Photography'},
                {'label': 'Crafts', 'value': 'Crafts'},
                {'label': 'Journalism', 'value': 'Journalism'},
                {'label': 'Dance', 'value': 'Dance'}
            ], 
            value = 'Dance', 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Currency'),
        dcc.Dropdown(
            id='currency', 
            options = [
                {'label': 'USA', 'value': 'USA'}, 
                {'label': 'UK', 'value': 'UK'}, 
                {'label': 'Europe', 'value': 'Europe'}, 
                {'label': 'Canada', 'value': 'Canada'}, 
                {'label': 'Australia', 'value': 'Australia'}, 
            ], 
            value = 'USA', 
            className='mb-5', 
        ),
        dcc.Markdown('#### State'), 
        dcc.Slider(
            id='state', 
            min=0, 
            max=1, 
            step=1, 
            value=1, 
            marks={n: str(n) for n in range(0, 1, 1)}, 
            className='mb-5', 
        ),
        dcc.Markdown('#### USD Goal Real'), 
        dcc.Slider(
            id='usd_goal_real', 
            min=0, 
            max=166361400, 
            step=1000, 
            value=0, 
            marks={n: str(n) for n in range(0,166361400, 1000)}, 
            className='mb-5', 
        ),
        dcc.Markdown('#### Length Days'), 
        dcc.Slider(
            id='dB', 
            min=1, 
            max=92, 
            step=4, 
            value=33, 
            marks={n: str(n) for n in range(1,92,4)}, 
            className='mb-5'
        )
    ],
    md=4
)


column2 = dbc.Col(
    [
        #html.H2('Success Prediction', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])