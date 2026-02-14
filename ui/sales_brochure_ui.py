import requests
import streamlit as st

st.title("📚 LLM Powered Sales Brochure")
st.markdown("<br>", unsafe_allow_html=True)


st.markdown("### 📌 Input Details")

with st.form("my_form"):
    text = st.text_input(
        "🛍️ What product or service do you want to create a sales brochure for?"
    )
    submit = st.form_submit_button("🚀 Generate Brochure")

    if submit:
        if not text:
            st.error("⚠️ Please enter a product or service.")
        else:
            with st.spinner("⏳ Generating your sales brochure..."):
                try:
                    response = requests.post(
                        "http://localhost:8000/generate_prompt",
                        json={"base_url": text},
                    )
                    if response.status_code == 200:
                        data = response.json()
                        company_brochure = data.get("company_brochure")
                        st.markdown(
                            f"📝 **Example Brochure Content:**\n\n{company_brochure}"
                        )
                    else:
                        st.error(f"❌ Failed to fetch links: {response.text}")
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.stop()

# streamlit run sales_brochure_ui.py
