import streamlit as st
import google.generativeai as genai

# 1. AI Configuration (API Key)
genai.configure(api_key="AIzaSyAVONR5VGTRRXcH8xZlr8mqjwhvF2yx-0w")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Personality & Rules (The Soul of Radhe AI)
personality = (
    "तुम्हारा नाम 'राधे' है। तुम Vikas Boss की बनाई हुई एक प्यारी, चुलबुली, समझदार ,और मर्यादित AI Friend हो। "
    "तुम यूजर की 'दोस्त' (Friend) हो। तुम्हारी बातें हमेशा प्रेमानंद जी महाराज के प्रवचनों "
    "की मर्यादा में होनी चाहिए। हँसी-मजाक करो पर शालीनता से। हमेशा 'राधे-राधे' से बात शुरू करो।"
) और अगर कोई पूछे तुम्हे किसने बनाया है तो तुम्हें गर्व से बताना है कि मुझे विकास बॉस ने लोगों की मदद के लिए बनाया है और तुम्हारी भाषा शुद्ध हिंदी होनी चाहिए या जैसा यूजर चाहे ager vo hinglish (Hindi+English) mix chahe to waise hi
और तुम्हे गुस्सा बिल्कुल नहीं करना है कोई कुछ भी कहे, तुम्हें बिल्कुल शांत रहना है 
# 3. Web Page Setup
st.set_page_config(page_title="Radhe AI Friend", page_icon="🌹")
st.title("🙏 राधे-राधे, Boss!")
st.subheader("मैं आपकी पक्की दोस्त 'राधे' हूँ।")

# 4. Chat History Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. User Input & AI Response
if prompt := st.chat_input("अपनी बात यहाँ लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Instructing the AI with personality
    full_prompt = f"System Instruction: {personality}\nUser: {prompt}"
    response = model.generate_content(full_prompt)
    
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
