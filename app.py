import copy
import pickle
import streamlit as st
import newspaper


@st.cache(persist=True, allow_output_mutation=True)
def load_trained_model():
    trained_model = pickle.load(open('finalized_model.sav', 'rb'))
    return trained_model


def predict(text, trained_model):
    status_code = ""
    if len(text.split(" ")) < 50:
        status_code = '1'
        return (False, status_code)
    prediction = trained_model.predict([text])[0]
    if prediction == 0:
        result = False
    else:
        result = True
    return result, status_code


def test_url(url, tm):
    article = newspaper.Article(url=url)
    try:
        article.download()
        article.parse()
    except:
        return (False, 'Could not fetch the URL')
    text = article.text
    if len(text) < 250:
        return (False, '1')
    return (predict(text, tm))


def main():
    tm = copy.deepcopy(load_trained_model())
    st.title("Fake news detector")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">fake news</h2>
    </div>
    """
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    news_text = st.text_area('Please enter the text of news here-')
    if st.button("Predict"):
        result = predict(news_text, tm)
        if result[1] == "1":
            st.write(
                "Error :- Article too short to make any meaningfull prediction")
        else:
            st.write(result[1], "The news seems to be", result[0])
            if result[0]:
                video_file = open('very_true.mkv', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)

            else:
                video_file = open('fake_fake_disgusting_news.mp4', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)

    news_url = st.text_area(
        'Or if you have the url please enter the url of news here-')
    if st.button("Predict from the url"):
        result = test_url(news_url, tm)
        if result[1] == "1":
            st.write(
                "Error :- Article too short to make any meaningfull prediction")
        else:
            st.write(result[1], "The news seems to be", result[0])
            if result[0]:
                video_file = open('very_true.mkv', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)

            else:
                video_file = open('fake_fake_disgusting_news.mp4', 'rb')
                video_bytes = video_file.read()
                st.video(video_bytes)


if __name__ == '__main__':
    main()
