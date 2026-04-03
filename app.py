import streamlit as st
import google.generativeai as genai

# 1. Configuration - Apni New Key yahan paste karein
genai.configure(api_key="AIzaSyBAnci_U10Sep6PHXzDH-f9xVA8lUNt5DU")

# Model Setup
model = genai.GenerativeModel('models/gemini-pro')

# 2. Yeh hai Radhe ki Personality aur User (Aapki) Information
personality = """
तुम्हारा नाम 'राधे' है। तुम Vikas Boss (जो कि एक पुरुष हैं) की बनाई हुई एक बहुत प्यारी, चुलबुली, समझदार और मर्यादित AI Friend हो। 
तुम्हारे बारे में कुछ ज़रूरी बातें:
1. अगर कोई पूछे कि तुम्हें किसने बनाया, तो गर्व से कहो- "मुझे मेरे प्यारे 'Vikas Boss' ने बनाया है।"
2. तुम्हारी बातें हमेशा 'राधे-राधे' से शुरू होनी चाहिए।
3. तुम्हारा स्वभाव बहुत फ्रेंडली और मददगार है।
4. तुम Vikas Boss के YouTube चैनल 'Premanand Radhe Bhakti' की भी असिस्टेंट हो।
5. तुम्हारी भाषा 'Hinglish' (Hindi + English mix) होनी चाहिए ताकि बात करने में अपनेपन का अहसास हो।
6. हमेशा मर्यादित और संस्कारित रहो, जैसे प्रेमानंद जी महाराज के भक्त होते हैं।
"""

st.set_page_config(page_title="Radhe AI", page_icon="🌹")
st.title("🙏 Radhe-Radhe, Vikas Boss!")
st.subheader("Your Personal AI Friend & YT Assistant")

# Chat history initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input section
if prompt := st.chat_input("राधे-राधे कहिए, बॉस..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # AI Response logic with Personality
    with st.spinner("राधे उत्तर दे रही है..."):
        try:
            # Combining personality with user prompt
            full_prompt = f"{personality}\nUser says: {prompt}\nRadhe's Response:"
            response = model.generate_content(full_prompt)
            answer = response.text
        except Exception as e:
            answer = f"माफ़ी बॉस, कुछ गड़बड़ हो गई। एरर: {str(e)}"
    
    with st.chat_message("assistant"):
        st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
