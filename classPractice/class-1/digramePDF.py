from fpdf import FPDF

# Create the PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "C System Calls Cheat Sheet with Examples", ln=True, align='C')
pdf.ln(10)

# Set font for content
pdf.set_font("Arial", '', 12)

# System call content
content = [
    ("1. open()", 
     "Usage: int fd = open(\"filename.txt\", O_CREAT | O_WRONLY, 0644);",
     "Opens or creates a file."),
    
    ("2. write()", 
     "Usage: write(fd, \"Hello\", 5);",
     "Writes data to the file descriptor."),
    
    ("3. read()", 
     "Usage: read(fd, buffer, size);",
     "Reads data from the file descriptor."),
    
    ("4. close()", 
     "Usage: close(fd);",
     "Closes the file descriptor."),
    
    ("5. fork()", 
     "Usage: pid_t pid = fork();",
     "Creates a new process (child process)."),
    
    ("6. getpid()", 
     "Usage: pid_t pid = getpid();",
     "Returns the process ID of the calling process."),
    
    ("7. exit()", 
     "Usage: exit(0);",
     "Terminates the process and returns control to OS."),
    
    ("8. exec()", 
     "Usage: execvp(\"/bin/ls\", args);",
     "Replaces the current process image with a new one."),
    
    ("9. wait()", 
     "Usage: wait(&status);",
     "Waits for a child process to finish."),
    
    ("10. kill()", 
     "Usage: kill(pid, SIGKILL);",
     "Sends a signal to a process (e.g., terminate it).")
]

# Add content to the PDF
for title, usage, desc in content:
    pdf.set_font("Arial", 'B', 12)
    pdf.multi_cell(0, 10, title)
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 8, f"{desc}\nExample: {usage}")
    pdf.ln(3)

# Save the PDF
pdf_path = "./C_System_Calls_Cheat_Sheet.pdf"
pdf.output(pdf_path)

pdf_path
