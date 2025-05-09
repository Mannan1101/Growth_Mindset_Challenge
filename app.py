import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="centered")

st.title("🌱 Growth Mindset Challenge Web App")
st.subheader("Unlock Your Potential with a Growth Mindset")

st.markdown("""
A **growth mindset** is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from mistakes.

> *"The view you adopt for yourself profoundly affects the way you lead your life."* – Carol Dweck

---

### 🌟 Why Adopt a Growth Mindset?

- ✅ **Embrace Challenges** – Obstacles help you grow.
- ✅ **Learn from Mistakes** – Every mistake is a lesson.
- ✅ **Persist Through Difficulties** – Keep going even when it's hard.
- ✅ **Celebrate Effort** – Effort matters more than results.
- ✅ **Stay Curious** – Always be ready to learn.

---

### 🧠 How to Practice a Growth Mindset

1. Set learning goals, not just performance goals.
2. Reflect on what you learned daily.
3. Ask for feedback and improve.
4. Encourage yourself and your peers.
""")

st.markdown("---")

if st.button("💬 Get a Motivation Quote"):
    st.success("“Challenges are what make life interesting. Overcoming them is what makes life meaningful.” – Joshua J. Marine")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
