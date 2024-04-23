# UI

import streamlit as st
import pandas as pd



def main():
    df = pd.read_csv('./data/iris.csv')
    
    # 버튼 만들기
    # 유저가 버튼을 누르면 데이터프레임을 보여준다
    if st.button('데이터 보기'):
        st.dataframe(df)
    
    # '대문자' 버튼을 만들고
    # 버튼을 누르면 species컬럼의 값들을 대문자로
    # 변경한 데이터프레임을 화면에 띄워라
    
    if st.button('대문자'):
        st.write(df['species'].str.upper())
    else :
        st.text('누르세욧')
        
    # 라디오버튼 : 여러개 중 한개 선택할때
    my_order = ['오름차순 정렬','내림차순 정렬']
    status = st.radio('정렬 방법 선택', my_order)
    
    # print(status)
    
    # petal_length 컬럼으로 정렬해서 df 보여준다
    if status == my_order[0] :
        st.dataframe(df.sort_values('petal_length', ascending= True))
    elif status == my_order[1] :
        st.dataframe(df.sort_values('petal_length', ascending= False))
    
    
    # 체크박스 : 둘중 하나만 선택하게끔 만들때 (체크 및 해제)
    # 체크하면 헤드5개 보여주고 해제하면 안보여주도록
    if st.checkbox('헤드 5개 보기') :
        st.dataframe( df.head() )
    
    # 셀렉트 박스 : 여러개에서 한개만 고르되
    #            : 리스트가 많을때 사용한다
    language = ['Python','C','Java','Go','PHP','Dart']
    my_choice = st.selectbox('좋아하는 언어 선택',language)
    if my_choice == language[0] or my_choice == language[2] :
        st.text('정말 재미있는 언어입니다')
    elif my_choice == language[3] or my_choice == language[5] :
        st.text('배우고 싶습니다')
    else :
        st.text('오래된 언어입니다')
    
    # 멀티 셀렉트 : 여러개중 여러개를 선택하게 할떄
    # 유저가 선택한걸 데이터프레임으로 보여주되
    # 아무것도 선택하지 않으면 아무것도 나오지 않게 하시오
    choice_list = st.multiselect('원하는 컬럼을 선택하세요', df.columns)
    if choice_list :
        st.dataframe( df[choice_list] )
    else:
        st.write(" ")
        
    # 슬라이더 : 숫자 조정하는데 주로 사용
    # 나이를 슬라이더로 입력 받는다
    # 1세부터 120세까지 입력받을 수 있도록 한다
    # 선택한 나이가 웹 화면에 출력되도록 한다
    my_age = st.slider('나이 선택', 1, 120, 1, 1)
    st.info(f'제 나이는 {my_age} 세 입니다')
    
    # 익스펜더
    with st.expander('hello'):
        st.text('데이터프레임입니다')
        st.dataframe(df)

    
    
    
    

if __name__ == '__main__' :
    main()