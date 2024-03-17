import streamlit as st
from reportlab.pdfgen import canvas
from PIL import Image
import os

def main():
    st.title("Image To PDF Converter")

    uploaded_files = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

    output_pdf_name = st.text_input("Enter output PDF name:", "output")

    if st.button("Convert To PDF") and uploaded_files:
        pdf = canvas.Canvas(f"{output_pdf_name}.pdf", pagesize=(612, 792))

        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width / img.width, available_height / img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width) / 2
            y_centered = (792 - new_height) / 2

            pdf.setFillColorRGB(255, 255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()

        pdf.save()
        st.success(f"PDF '{output_pdf_name}.pdf' created successfully.")

        # Provide download link for the generated PDF
        with open(f"{output_pdf_name}.pdf", "rb") as f:
            pdf_bytes = f.read()
        st.download_button(label="Download PDF", data=pdf_bytes, file_name=f"{output_pdf_name}.pdf", mime="application/pdf")

if __name__ == "__main__":
    main()
