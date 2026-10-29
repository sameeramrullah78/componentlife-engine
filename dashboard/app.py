from pathlib import Path
import sys
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from componentlife.pipeline import assess_component
from componentlife.reporting.report_generator import to_markdown

REFERENCE = ROOT / "data/demo_reference/reference_profiles.csv"
SAMPLES = {
    "Healthy alternator": ROOT / "data/demo_tests/healthy_alternator.csv",
    "Degraded alternator": ROOT / "data/demo_tests/degraded_alternator.csv",
    "Uncertain alternator": ROOT / "data/demo_tests/uncertain_alternator.csv",
}

st.set_page_config(page_title="ComponentLife v0.1", page_icon="⚙️", layout="wide")
st.title("ComponentLife — Degradation Fingerprint & Confidence Engine")
st.caption("Proof of concept using synthetic alternator data. Not a certified serviceability or remaining-life assessment.")
choice = st.selectbox("Demo component", list(SAMPLES))
path = SAMPLES[choice]
result = assess_component(path, REFERENCE)
df = pd.read_csv(path)

c1, c2, c3 = st.columns(3)
c1.metric("Condition", result["classification"]["category"].replace("_", " ").title())
c2.metric("Confidence", f"{result['confidence']['score']:.1f}%")
c3.metric("Detected anomalies", len(result["anomalies"]))

st.subheader("Degradation fingerprint")
labels = [k.replace("_", " ").title() for k in result["fingerprint"]]
values = [result["fingerprint"][k] for k in result["fingerprint"]]
fig = go.Figure()
fig.add_trace(go.Scatterpolar(r=values + [values[0]], theta=labels + [labels[0]], fill="toself", name="Component"))
fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=430)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Sensor traces")
st.line_chart(df.set_index("timestamp")[["voltage", "current", "ripple_mv", "vibration_rms", "temp_c"]])

left, right = st.columns(2)
with left:
    st.subheader("Confidence factors")
    st.dataframe(pd.DataFrame([
        {"factor": "Data quality", "score": result["confidence"]["data_quality"]},
        {"factor": "Repeatability", "score": result["confidence"]["repeatability"]},
        {"factor": "Reference coverage", "score": result["confidence"]["reference_coverage"]},
        {"factor": "Signal agreement", "score": result["confidence"]["signal_agreement"]},
    ]), hide_index=True, use_container_width=True)
with right:
    st.subheader("Anomalies")
    if result["anomalies"]:
        st.dataframe(pd.DataFrame(result["anomalies"]), hide_index=True, use_container_width=True)
    else:
        st.success("No warning-level anomalies detected against the demo reference profile.")

st.subheader("Explainable report")
st.markdown(to_markdown(result))
st.warning("The included reference profile and sample datasets are synthetic / illustrative. Do not use this prototype to certify an automotive component.")
