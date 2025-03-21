# Re-try PDF generation with restricted characters (remove unicode arrows)
from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Practice Problem: Cloud App Expansion Scenario", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", '', 12)
# Problem Description
problem_description = """
You have a new cloud-based application with the following details:

Functions and Capacity per Server:
- Data Analysis: 600 records/min
- File Upload: 250 files/min
- Chat Messaging: 400 messages/min

System Configuration:
- Servers available: 4

Current User Demand:
- Data Analysis: 1,200 records
- File Upload: 800 files
- Chat Messaging: 1,000 messages

Latency:
- Data Analysis: 150 ms
- File Upload: 250 ms
- Chat Messaging: 100 ms

Failure Rates:
- Data Analysis: 1.5%
- File Upload: 0.5%
- Chat Messaging: 1.0%

Server Costs:
- First Server = $3,000
- Each Additional Server = $2,000

New Demand Forecast:
- Data Analysis: 3,000 records
- File Upload: 1,500 files
- Chat Messaging: 2,000 messages
"""

pdf.multi_cell(0, 10, problem_description)
pdf.ln(5)

# Questions Section
pdf.set_font("Arial", 'B', 13)
pdf.cell(0, 10, "Practice Questions:", ln=True)
pdf.set_font("Arial", '', 12)

questions = [
    "1. Calculate total throughput for each functionality with 4 servers.",
    "2. What is the latency for 3 users requesting file uploads simultaneously?",
    "3. If new demand is: Data = 3000, File = 1500, Chat = 2000 - How many additional servers needed for each service?",
    "4. Calculate 20-day reliability for each service.",
    "5. What is total current cost and the cost for scaling to meet full demand?"
]

for question in questions:
    pdf.multi_cell(0, 10, question)

# Save the PDF
pdf_path = "./Cloud_App_Expansion_Practice_Problem.pdf"
pdf.output(pdf_path)

pdf_path
