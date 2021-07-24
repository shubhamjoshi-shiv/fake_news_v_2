import copy
import pickle
import streamlit as st


@st.cache(persist=True, allow_output_mutation=True)
def load_trained_model():
    trained_model = pickle.load(open('finalized_model.sav', 'rb'))
    return trained_model


def predict(text, trained_model):
    prediction = trained_model.predict([text])[0]
    if prediction == 0:
        result = False
    else:
        result = True
    return result


def main():
    tm = copy.deepcopy(load_trained_model())
    st.title("fake news detector v-23")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
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

    news_text = st.text_area('plese enter the text of news here-')
    if st.button("Predict"):
        result = predict(news_text, tm)
        st.write("the news seems to be",result)


if __name__ == '__main__':
    main()
