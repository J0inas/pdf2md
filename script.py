from pdf2image import convert_from_path

# this variable should not be changed in the process
# md_path = "/Users/joinas/Documents/Obsidian/Life"
md_path = "/Users/joinas/Documents/Uni/Semester 8/pdf2md/"
# gets changed in the process
pdf_name_and_path = ".pdf"
lecture_title = "title"
lecture_number = ""
# those are recommandations for the user to put in
current_modules = {"PGP", "WR", "SiSy", "Chip-Krieg", "Frontend-Entwicklung"}

# Use "input" for text input and create your new md file from images
print("HELLO, welcome to //PDF2MD\\" + "\n" + "Please select your module")
print(current_modules)
module_name = "a module" 

module_name = input()
print("Very well then." + "\n")
    
print("Please drag your file name into the console.")

pdf_name_and_path = input()
pages = convert_from_path(pdf_name_and_path.replace("'", ""))

for slides_num, page in enumerate(pages):
    page.save(f'{md_path}{module_name} {lecture_number} - {slides_num}.png', 'PNG')
    
print ("File sucessfully turned into PNGs." + "\n")

print ("Almost done now." + "\n")

print ("Which lecture is this? Please enter a number like so '07'" + "\n")

lecture_number = input()

print("Oh and what is the name of the lecture? Please enter its name" + "\n")

lecture_title = input ()

md_path += f"/ {lecture_number} {lecture_title}.md"

# open markdown file and write content:
with open(md_path, 'w') as file:
    for current_slide in range(0, slides_num + 1):
        file.write(f'![[{module_name} {lecture_number} - {current_slide}.png]]' + "\n")

# print completion message
print('\rFile created succesfully.')