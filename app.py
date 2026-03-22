import streamlit as st
import pickle
import pandas as pd

teams = ['Chennai Super Kings',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Delhi Capitals',
 'Rajasthan Royals',
 'Sunrisers Hyderabad',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans']

cities = ['Bangalore', 'Hyderabad', 'Bengaluru', 'Mumbai', 'Indore',
       'Kolkata', 'Delhi', 'Chandigarh', 'Chennai', 'Jaipur', 'Pune',
       'Visakhapatnam', 'Abu Dhabi', 'Ahmedabad', 'Sharjah', 'Dubai',
       'Navi Mumbai', 'Lucknow', 'Guwahati', 'Dharamsala', 'Mohali',
       'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Cuttack', 'Nagpur', 'Raipur', 'Ranchi', 'New Chandigarh']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL win Prediction (Based on 2008 - 2025 data)')
st.text('Build by: Nilay Mallik, Miltan Biswas(23053874), Aditya Palit, Satish Prajapati')

col1, col2 = st.columns(2)

with col1:
    team_batting = st.selectbox('Select the batting team',teams)

with col2:
    team_bowling = st.selectbox('Select the bowling team',teams)

city = st.selectbox('Select the city', cities)

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets_left = 10 - wickets
    crr	= score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'team_batting':[team_batting],
                  'team_bowling':[team_bowling],
                  'city':[city],
                  'runs_left':[runs_left],
                  'balls_left':[balls_left],
                  'wickets_left':[wickets_left],
                  'crr':[crr],
                  'rrr':[rrr]})
    st.table(input_df)
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(team_batting + "-" + str(round(win*100)) + "%")
    st.header(team_bowling + "-" + str(round(loss*100)) + "%")

