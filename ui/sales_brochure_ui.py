import streamlit as st
import requests

st.title("📚 LLM Powered Sales Brochure")
st.markdown("<br>", unsafe_allow_html=True)


textword = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
    "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
    "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia "
    "deserunt mollit anim id est laborum."
)

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
                        "http://localhost:8000/fetch_links",
                        json={"base_url": text},
                    )
                    if response.status_code == 200:
                        data = response.json()
                        links = data.get("links", [])
                        st.write(f"📝 Example brochure content:\n\n{links}")
                    else:
                        st.error(f"❌ Failed to fetch links: {response.text}")
                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.stop()

# streamlit run sales_brochure_ui.py