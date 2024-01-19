from docx import Document

def process_linux_commands(input_filename, output_filename):
    unique_commands_list = []

    doc = Document(input_filename)
    for paragraph in doc.paragraphs:
        command = paragraph.text.strip().split(' ', 1)[1]

        # Check for duplicates before adding to the list
        if command not in unique_commands_list:
            unique_commands_list.append(command)

    # Write unique commands to the output file while maintaining the sequence
    with open(output_filename, 'w') as output_file:
        num = 1
        for unique_command in unique_commands_list:
            output_file.write(f"{num}:  {unique_command}\n")
            num += 1

if __name__ == "__main__":
    input_filename = "linux_history.docx"  # Change this to your Linux command history .docx file name
    output_filename = "unique_commands.txt"  # Change this to your output file name

    process_linux_commands(input_filename, output_filename)
