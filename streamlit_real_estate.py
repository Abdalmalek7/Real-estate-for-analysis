import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout='wide',page_title='Egypt Real Estate')
df=pd.read_csv('real_estate_cleaned for analysis.csv')


page=st.sidebar.radio('pages',['Intro','Analysise'])

if page=='Intro':
    html_title = """<div style="color:orange;  text-align:center;font-size:70px; font-weight:bold;">
                        Egypt Real Estate Data Project 
                    </div>"""
    st.markdown(html_title, unsafe_allow_html=True)
    st.image('real2.jpg')
    intro='<span style="color:green; font-size:60px; font-weight:bold;">📊 Introduction</span>'
    st.markdown(intro, unsafe_allow_html=True)
    html_intro= """

                <span style="font-size:18px;">
                In this project, we explored and cleaned a real estate dataset collected from <strong>Aqarmap</strong>, one of the largest real estate platforms in Egypt.  
                The main goal of this project was to <strong>prepare the data</strong> for future modeling by performing a comprehensive preprocessing phase.  

                This included:
                <ul>
                <li>Handling missing values</li>
                <li>Cleaning and standardizing columns</li>
                <li>Encoding categorical variables</li>
                <li>Extracting new features</li>
                <li>Converting types and correcting outliers</li>
                </ul>

                In addition to the preprocessing phase, we also performed some <strong>exploratory analysis</strong> by asking key <strong>analytical questions</strong> to uncover insights about real estate prices and patterns in Egypt.
                </span>"""
    
    st.markdown(html_intro, unsafe_allow_html=True)
    

    link='<span style="color:green; font-size:40px; font-weight:bold;">The link of data website</span>'
    st.markdown(link, unsafe_allow_html=True)
    st.page_link(page='https://aqarmap.com.eg/ar/for-sale/apartment/?page=128',label= 'Aqarmap',icon="🚨",use_container_width=True)
    
    show='<span style="color:green; font-size:40px; font-weight:bold;">show data</span>'
    st.markdown(show, unsafe_allow_html=True)
    st.dataframe(df)

    shape='<span style="color:green; font-size:40px; font-weight:bold;">Shape of Data</span>'
    st.markdown(shape, unsafe_allow_html=True)
    st.write(df.shape)
    
 
elif page== 'Analysise':
    html_title = """<h1 style="color:orange;text-align:center;"> analytical questions</h1>"""
    st.markdown(html_title, unsafe_allow_html=True)

    q1='<span style="color:green; font-size:30px; font-weight:bold;"> 1- What is the average price per meter in each city?</span>'
    st.markdown(q1, unsafe_allow_html=True)
    d=df.groupby('city')['price_per_meter'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)


    q2='<span style="color:green; font-size:30px; font-weight:bold;"> 2- What is the top 5 regions these have highst price per meter ?</span>'
    st.markdown(q2, unsafe_allow_html=True)
    d=df.groupby('region')['price_per_meter'].mean().sort_values(ascending=False).head(5)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)


    q3='<span style="color:green; font-size:30px; font-weight:bold;">3- What is the impact of being in a compound on price and area? </span>'
    st.markdown(q3, unsafe_allow_html=True)
    d=df.groupby('in_compound')['price'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)
    

    q4='<span style="color:green; font-size:30px; font-weight:bold;">4- What is the most common type of housing unit? </span>'
    st.markdown(q4, unsafe_allow_html=True)
    d=df.type_of_unite.value_counts().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)
    

    q5='<span style="color:green; font-size:30px; font-weight:bold;"> 5- What is the average <span style="color:orange;">price</span> for each unit type?</span>'
    st.markdown(q5, unsafe_allow_html=True)
    d=df.groupby('type_of_unite')['price'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)


    q6='<span style="color:green; font-size:40px; font-weight:bold;"> 6- What is the average <span style="color:orange;">price_per_meter</span> for each unit type?</span>'
    st.markdown(q6, unsafe_allow_html=True)
    d=df.groupby('type_of_unite')['price_per_meter'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)

    q7='<span style="color:green; font-size:40px; font-weight:bold;">7- What is the effect of owner type (developer, broker, direct owner) on price? </span>'
    st.markdown(q7, unsafe_allow_html=True)
    d=df.groupby('owner_type')['price'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)

    q8='<span style="color:green; font-size:40px; font-weight:bold;">8- What is the difference in rooms and area across different building_category? </span>'
    st.markdown(q8, unsafe_allow_html=True)
    d=df.groupby('building_category')['rooms'].agg(lambda x : x.mode()[0] if len(x)>0 else np.nan).sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)

    q9='<span style="color:green; font-size:40px; font-weight:bold;">9- What is the average number of rooms for each area category? </span>'
    st.markdown(q9, unsafe_allow_html=True)
    d=df.groupby('area_category')['rooms'].mean().sort_values(ascending=False)
    fig=px.bar(data_frame=d ,x=d.index ,y=d.values )
    st.plotly_chart(fig)


    q10='<span style="color:green; font-size:40px; font-weight:bold;">10- What is the moste frequint viewe in each city? </span>'
    st.markdown(q10, unsafe_allow_html=True)
    d=df.groupby('city')['views'].agg(lambda x : x.mode()[0] if len(x)>0 else np.nan).sort_values(ascending=False).reset_index()
    st.dataframe(d)

