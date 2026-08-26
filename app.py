import streamlit as st
import pandas as pd
import tempfile
import os

from day26 import analyze_resume
from day26 import extract_job_skills


st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Screening Tool")
st.write(
    "Upload resumes and match them against a Job Description."
)

# Job Description
st.subheader("📋 Job Description")

job_description = st.text_area(
    "Paste the Job Description here:",
    height=200
)

# Resume upload
st.subheader("📄 Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload TXT resumes",
    type=["txt"],
    accept_multiple_files=True
)


if st.button("🔍 Screen Resumes"):

    if not job_description:
        st.warning("Please enter a Job Description.")

    elif not uploaded_files:
        st.warning("Please upload at least one resume.")

    else:

        required_skills = extract_job_skills(
            job_description
        )

        results = []

        for uploaded_file in uploaded_files:

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".txt"
            ) as temp:

                temp.write(
                    uploaded_file.getvalue()
                )

                temp_path = temp.name

            result = analyze_resume(
                temp_path,
                required_skills
            )

            results.append(result)

            os.remove(temp_path)

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Resume Match Score",
            ascending=False
        )

        df["Rank"] = range(1, len(df) + 1)

        st.success("Resume screening completed!")

        st.subheader("🏆 Candidate Ranking")

        st.dataframe(
            df,
            use_container_width=True
        )

        # Top candidate
        if len(df) > 0:

            st.subheader("🥇 Top Candidate")

            top = df.iloc[0]

            st.metric(
                "Resume Match Score",
                f"{top['Resume Match Score']}%"
            )

            st.write(
                f"**Candidate:** {top['Name']}"
            )

            st.write(
                f"**Skills:** {top['Skills']}"
            )

        # Shortlisting
        shortlisted = df[
            df["Resume Match Score"] >= 50
        ]

        st.subheader("✅ Shortlisted Candidates")

        st.dataframe(
            shortlisted,
            use_container_width=True
        )

        # CSV export
        csv = shortlisted.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Download Shortlisted Candidates",
            data=csv,
            file_name="shortlisted_candidates.csv",
            mime="text/csv"
        )