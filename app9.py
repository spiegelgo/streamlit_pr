import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def main() :
    st.title('차트 그리기 1')
    
    df = pd.read_csv('./data/iris.csv')
    st.dataframe(df)
    
    fig1 = plt.figure()
    plt.scatter(data=df, x='sepal_length',y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig1)
    
    fig2 = plt.figure()
    sb.scatterplot(data=df, x='sepal_length',y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig2)
    
    fig3 = plt.figure()
    sb.regplot(data=df, x='sepal_length',y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig3)
    
    # sepal_length 로 히스토그램을 그린다
    # bins의 갯수는 20개로
    
    fig4 = plt.figure()
    plt.hist(data=df, x='sepal_length',bins= 20, rwidth = 0.8)
    plt.title('histogram')
    plt.xlabel('sepal_length')
    plt.ylabel('count')
    st.pyplot(fig4)
    
    # sepal_length 히스토그램을 그리되
    # bins의 갯수를 10개와 20개로
    # 두개의 차트를 수평으로 보여달라
    
    fig5 = plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.hist( data=df, x='sepal_length', rwidth=0.8, bins= 10 )
    plt.title('bins 10')
    plt.xlabel('sepal_length')
    plt.ylabel('count')
    plt.subplot(1,2,2)
    plt.hist( data=df, x='sepal_length', rwidth=0.8, bins = 20 )
    plt.title('bins 20')
    plt.xlabel('sepal_length')
    plt.ylabel('count')
    st.pyplot(fig5)
    
    # 판다스의 데이터프레임의 차트도 그릴수 있다
    # species는 각각 몇개 인지 나타내시오
    # print(df['species'].value_counts())
    # 위의 결과를 바 차트로 나타내시오
    fig6 = plt.figure()
    df['species'].value_counts().plot(kind='barh')
    st.pyplot(fig6)

    # sepal_length 컬럼을 히스토그램으로 나타내시오
    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)
    
    # df의 상관계수를 구해서 차트로 표시
    fig8 = plt.figure()
    sb.heatmap(data = df.corr(numeric_only=True),vmin = -1, vmax = 1, annot = True, fmt='.1f')
    st.pyplot(fig8)

    
    
    
    

if __name__ == '__main__':
    main()