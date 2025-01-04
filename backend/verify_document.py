# backend/verify_document.py

import pytesseract # type: ignore
from PIL import Image # type: ignore
import sys

def verify_document(image_path):
    # Load the image from file
    img = Image.open(image_path)
    
    # Extract text using Tesseract
    extracted_text = pytesseract.image_to_string(img)
    
    # Example check for Aadhaar card or similar documents
    if "Aadhaar" in extracted_text:
        return "Document is valid"
    else:
        return "Document is invalid"

if __name__ == "__main__":
    image_path = sys.argv[1]
    result = verify_document(image_path)
    print(result)
# # backend/verify_document.py

# import pytesseract # type: ignore
# from PIL import Image # type: ignore
# import sys

# def verify_document(image_path):
#     # Load the image from file
#     img = Image.open(image_path)
    
#     # Extract text using Tesseract
#     extracted_text = pytesseract.image_to_string(img)
    
#     # Example check for Aadhaar card or similar documents
#     if "Aadhaar" in extracted_text:
#         return "Document is valid"
#     else:
#         return "Document is invalid"

# if __name__ == "__main__":
#     image_path = sys.argv[1]
#     result = verify_document(image_path)
#     print(result)
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches

# # Create a figure for the flowchart
# fig, ax = plt.subplots(figsize=(10, 12))

# # Helper function to create boxes and arrows
# def draw_box(text, x, y, box_type="rectangle", width=3, height=1.5, fontsize=10):
#     if box_type == "rectangle":
#         box = mpatches.Rectangle((x - width / 2, y - height / 2), width, height, edgecolor="black", facecolor="lightblue")
#     elif box_type == "decision":
#         box = mpatches.RegularPolygon((x, y), numVertices=4, radius=1.5, orientation=0.78, edgecolor="black", facecolor="lightgreen")
#     ax.add_patch(box)
#     ax.text(x, y, text, ha="center", va="center", fontsize=fontsize)

# def draw_arrow(x1, y1, x2, y2):
#     ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
#                 arrowprops=dict(facecolor="black", edgecolor="black", shrinkA=0, shrinkB=0, width=0.5))

# # Adding components to the flowchart
# draw_box("Start", 0, 10, box_type="rectangle")

# draw_box("User Accesses Web App", 0, 8, box_type="rectangle")
# draw_arrow(0, 9.25, 0, 8.75)

# draw_box("Interact with AI Chatbot for Scheme Discovery", 0, 6, box_type="rectangle", width=7)
# draw_arrow(0, 7.25, 0, 6.75)

# draw_box("Eligibility Check", 0, 4, box_type="decision")
# draw_arrow(0, 5.25, 0, 4.75)

# draw_box("Eligible?", -4, 4, box_type="rectangle")
# draw_arrow(0, 4, -2.5, 4)

# draw_box("Document Upload & OCR Verification", 0, 2, box_type="rectangle", width=7)
# draw_arrow(0, 3.25, 0, 2.75)

# draw_box("Documents Valid?", 0, 0, box_type="decision")
# draw_arrow(0, 1.25, 0, 0.75)

# draw_box("Submit Application", 0, -2, box_type="rectangle")
# draw_arrow(0, -0.75, 0, -1.75)

# draw_box("Track Progress", 0, -4, box_type="rectangle")
# draw_arrow(0, -2.75, 0, -3.75)

# draw_box("End", 0, -6, box_type="rectangle")
# draw_arrow(0, -4.75, 0, -5.75)

# # Adding annotations for decision branches
# draw_arrow(0, 4, 2.5, 4.75)  # No branch from eligibility check
# draw_box("Ineligible - Inform User", 4, 4, box_type="rectangle")

# draw_arrow(0, 0, 2.5, -0.75)  # No branch from document validation
# draw_box("Invalid Documents - Retry", 4, 0, box_type="rectangle")

# # Configure plot appearance
# ax.set_xlim(-6, 6)
# ax.set_ylim(-7, 11)
# ax.axis("off")

# # Display the flowchart
# plt.show()
