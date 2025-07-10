import streamlit as st
from core.analyzer import get_fastest_laps
from utils.plotting import plot_fastest_laps

# Page settings
st.set_page_config(
    page_title="F1 Fastest Lap Visualizer 🏁",
    layout="centered"
)

st.title("🏎️ F1 Fastest Lap Visualizer")
st.markdown("Compare the fastest lap times of each driver in any Formula 1 session using FastF1 data.")

# ---- User Inputs ----
year = st.selectbox("Select Year", list(range(2025, 2017, -1)))
gp = st.text_input("Enter Grand Prix (e.g. Silverstone, Monza)", "Silverstone")
session = st.selectbox("Select Session", ["FP1", "FP2", "FP3", "Q", "R"])

# ---- Action Button ----
if st.button("🔍 Analyze"):
    with st.spinner("Fetching data from FastF1 servers..."):
        try:
            # Fetch and process fastest laps
            df = get_fastest_laps(year, gp, session)

            if df.empty:
                st.warning("⚠️ No lap data available for this session. Try a different session or year.")
            else:
                st.success("✅ Fastest laps loaded successfully!")
                fig = plot_fastest_laps(df)
                st.pyplot(fig)

        except RuntimeError as err:
            st.error(f"⚠️ {err}")

        except Exception as e:
            st.error("❌ Unexpected error occurred while processing.")
            st.exception(e)
