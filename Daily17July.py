"""
Project Task
Build a Streamlit app that:

✅ Lets users upload either a CSV or an Excel (.xlsx) file.
✅ Detects which type of file they uploaded.
✅ Converts:

CSV → Excel

Excel → CSV
✅ Displays the data in a nice table.
✅ Provides a download button so they can instantly get the converted file.

This is an awesome way to practice:

File uploads and downloads in Streamlit,

Working with pandas DataFrames,

Converting data formats (CSV ↔ Excel),

And giving users a polished, interactive experience.
"""
import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="CSV ↔ Excel Converter")
st.title("📂 CSV ↔ Excel Converter")

uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        file_name = uploaded_file.name.lower()

        if file_name.endswith(".csv"):
            # Read and show CSV
            df = pd.read_csv(uploaded_file)
            st.success("✅ CSV file loaded successfully.")
            st.subheader("Preview of Uploaded CSV:")
            st.dataframe(df, use_container_width=True)

            # Convert to Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            output.seek(0)

            # Download as Excel
            st.download_button(
                label="⬇️ Download as Excel (.xlsx)",
                data=output,
                file_name="converted.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        elif file_name.endswith(".xlsx"):
            # Read and show Excel
            df = pd.read_excel(uploaded_file)
            st.success("✅ Excel file loaded successfully.")
            st.subheader("Preview of Uploaded Excel:")
            st.dataframe(df, use_container_width=True)

            # Convert to CSV
            csv_data = df.to_csv(index=False).encode("utf-8")

            # Download as CSV
            st.download_button(
                label="⬇️ Download as CSV (.csv)",
                data=csv_data,
                file_name="converted.csv",
                mime="text/csv"
            )

        else:
            st.error("❌ Unsupported file format.")
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
