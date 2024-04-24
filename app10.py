# 스트림릿의 내장 차트 함수와 유명한 라이브러리인 plotly 차트


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def main():
    # 스트림릿에서 제공해주는 차트
    # line_chart, area_chart
    df1 = pd.read_csv('./data/lang_data.csv')
    
    column_list = df1.columns[ 1 : ]
    choice_list = st.multiselect('언어를 선택하세요.', column_list)

    if len(choice_list) != 0:
        df_choice = df1[choice_list]
        
        st.dataframe(df_choice)
        
        fig = plt.figure()
        df_choice.plot()
        st.pyplot()
        
        st.line_chart(df_choice)
        
        st.area_chart(df_choice)
        # 스트림릿이 제공하는 bar_chart
        df2 = pd.read_csv('./data/iris.csv')
        df_iris = df2.iloc[ : , : -2+1]
        st.bar_chart(df_iris)
        
        # 스트림릿 제공 map차트(위도,경도)
        df3 = pd.read_csv('./data/location.csv',index_col = 0)
        st.map(df3)
        
        
        # plotly 의 pie차트
        df4= pd.read_csv('./data/prog_languages_data.csv',index_col= 0)
        print(df4)
        
        fig1 = px.pie(data_frame= df4, names='lang',values='Sum',title='각 언어별 pie차트')
        st.plotly_chart(fig1)
        
        # plotly의 bar차트
        df_sorted = df4.sort_values('Sum')
        fig2 = px.bar(data_frame= df_sorted, x='lang', y ='Sum')
        st.plotly_chart(fig2)
        
        


if __name__ == '__main__':
    main()