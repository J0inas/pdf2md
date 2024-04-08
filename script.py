from pdf2image import convert_from_path

# this variable should not be changed in the process
md_path = "/Users/joinas/Documents/Obsidian/Life/"
# local path
# md_path = "/Users/joinas/Documents/Uni/Semester 8/pdf2md/"
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
print(f"Very well then, {module_name} it is." + "\n")
    
print("Please drag your file name into the console.")

pdf_name_and_path = input()
pages = convert_from_path(pdf_name_and_path.replace("'", ""))
# TODO: Add a check here if the file was found // shouldnt be a problem tho if you drag it in

print ("\n" + "Which lecture is this? Please enter a number like so '07'")

lecture_number = input()

print("\n" + "Oh and what is the name of the lecture? Please enter its name")
# TODO: Add option to not get the lecture number
lecture_title = input ()

print ("Almost done now." + "\n")

for slides_num, page in enumerate(pages):
    page.save(f'{md_path}{module_name} {lecture_number} - {slides_num}.png', 'PNG')
    
print ("File sucessfully turned into PNGs." + "\n")

# TODO: A summary of all my inputs to check if it was correct and then type "y" to proceed or "n" to restart the process.
# print ("Great, to sum it up: ")
md_path += f"{lecture_number} {lecture_title}.md"

# open markdown file and write content:
with open(md_path, 'w') as file:
    for current_slide in range(0, slides_num + 1):
        file.write(f'![[{module_name} {lecture_number} - {current_slide}.png]]' + "\n")

# print completion message
print('\rFile created succesfully.')
print("\n Filepath:" + md_path)