from fpdf import FPDF

# Create PDF document for step-by-step solutions
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a Unicode-compatible font (e.g., DejaVuSans)
pdf.add_font("DejaVuSans", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVuSans", '', 12)

# Add title
pdf.set_font("DejaVuSans", 'B', 16)
pdf.cell(0, 10, "Step-by-Step Solutions: Cloud App Expansion Practice Problem", ln=True, align='C')
pdf.ln(10)
pdf.set_font("DejaVuSans", '', 12)

# Add solution content
solutions = [
    "1. Total Throughput Calculation with 4 Servers:",
    "- Data Analysis: 600 * 4 = 2,400 records/min",
    "- File Upload: 250 * 4 = 1,000 files/min",
    "- Chat Messaging: 400 * 4 = 1,600 messages/min",

    "2. Latency for 3 Users Requesting File Uploads:",
    "- Latency per user is independent and parallel.",
    "- Each user experiences 250 ms latency.",
    "- So, all 3 users have 250 ms latency each (not cumulative).",

    "3. Servers Needed for New Demand:",
    "- Data Analysis: 3,000 / 600 = 5 servers (Needs 1 extra server)",
    "- File Upload: 1,500 / 250 = 6 servers (Needs 2 extra servers)",
    "- Chat Messaging: 2,000 / 400 = 5 servers (Needs 1 extra server)",

    "4. 20-Day Reliability Calculation:",
    "- Formula: (1 - failure rate)^N",
    "- Data Analysis: (1 - 0.015)^20 ≈ 0.7397 = 73.97%",
    "- File Upload: (1 - 0.005)^20 ≈ 0.9048 = 90.48%",
    "- Chat Messaging: (1 - 0.01)^20 ≈ 0.8179 = 81.79%",

    "5. Cost Calculations:",
    "- Current Cost (4 Servers): $3,000 + (3 * $2,000) = $9,000",
    "- Scaled Costs:",
    "  • Data Analysis (5 Servers): $3,000 + (4 * $2,000) = $11,000",
    "  • File Upload (6 Servers): $3,000 + (5 * $2,000) = $13,000",
    "  • Chat Messaging (5 Servers): $3,000 + (4 * $2,000) = $11,000"
]

# Write solutions into the PDF
for line in solutions:
    pdf.multi_cell(0, 10, line)

# Save the PDF
solution_pdf_path = "./Cloud_App_Step_by_Step_Solutions.pdf"
pdf.output(solution_pdf_path)

# Print the path to the saved PDF
print(f"PDF saved to: {solution_pdf_path}")

# Optionally, open the PDF automatically (if running on a system with a PDF viewer)
import os
if os.name == 'nt':  # For Windows
    os.startfile(solution_pdf_path)
elif os.name == 'posix':  # For macOS and Linux
    os.system(f'open "{solution_pdf_path}"')