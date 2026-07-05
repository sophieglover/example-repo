if_folder="if_folder"
hyperionDev="hyperionDev"
new_projects="new-projects"
new_folder="new_folder"


# Write an if statement to create a new folder named if_folder if a folder
# named new_folder already exists.
if [ -d $new_folder ]; then
    mkdir $if_folder
    echo "Folder with the name $if_folder is created"

fi


# Within the same file, write an if-else statement to check whether a folder 
# named if_folder exists. If it does, create a new folder named hyperionDev
# otherwise, create a new folder named new-projects

if [ -d $if_folder ]; then
    mkdir $hyperionDev

else
    mkdir $new_projects
    echo "Folder with the name $new_projects is created"

fi