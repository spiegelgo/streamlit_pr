# 이미지/ 동영상/ 음악파일을 화면에 보여주는 법
import streamlit as st

# 이미지 처리를 위한 라이브러리
from PIL import Image
# PIL = Python Image Library


def main() :
    # 1. 저장되어있는 이미지파일 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')
    
    st.image(img)
    st.image(img, width = 500)
    st.image(img, use_column_width = True)
    
    # 1-2. 인터넷에 있는 이미지 화면에 표시하는 방법
    #    인터넷상의 이미지 : URL이 있다
    
    st.image('https://i.namu.wiki/i/JBHVazuS08hDQOZSQjSTa-_Wyk0O4pSE3IGNcBBj79TgYC1dQSfl39dnfn8bYdqxQqiP6XHj07RhzTWhIw6D1g.webp')
    url = 'https://i.namu.wiki/i/JBHVazuS08hDQOZSQjSTa-_Wyk0O4pSE3IGNcBBj79TgYC1dQSfl39dnfn8bYdqxQqiP6XHj07RhzTWhIw6D1g.webp'
    st.image(url)
    
    # 2. 저장된 비디오 동영상 표시방법
    video_file = open('./data/video1.mp4', 'rb')
    st.video(video_file)

    
    # 2-2. 인터넷에 있는 비디오 동영상 표시방법
    video_url = "https://www.example.com/video.mp4"
    st.video(video_url)

    # 2-3. 유튜브 영상 표시방법
    youtube_url = "https://youtu.be/tNYDJz6wdQ8?si=dTwIPGqqB39oV-bz"
    st.video(youtube_url)

    
    # 3. 오디오 음성파일 표시방법
    audio_file = open('./data/song.mp3','rb')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__ == '__main__' :
    main()