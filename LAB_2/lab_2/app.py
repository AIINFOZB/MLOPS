import streamlit as st
import joblib

# Load the model
spam_clf = joblib.load(open('./models/spam_detector_model.pkl', 'rb'))

# Load vectorizer
vectorizer = joblib.load(open('./vectors/vectorizer.pickle', 'rb'))


def main(title="Spam detection app".upper()):
    st.markdown("<h1 style='text-align: center; "
                "font-size: 60px; "
                "color: #4682B4;'>{}</h1>".format(title),
                unsafe_allow_html=True)
    st.image("./images/message-image.jpeg")
    info = ''

    with st.expander("Check if your text is a spam or ham 😀"):
        text_message = st.text_input("Please enter your message")
        if st.button("Predict"):
            prediction = spam_clf.predict(vectorizer.transform([text_message]))

            if prediction[0] == 0:
                info = 'Ham'

            else:
                info = 'Spam'
            st.success('Prediction: {}'.format(info))


if __name__ == "__main__":
    main()
