folder1="folder1"
folder2="folder2"
folder3="folder3"


# make a folder called folder1
if [ -d $folder1 ]; then
    echo "The folder named $folder1 already exists"

else
    mkdir $folder1
    echo "Folder with the name $folder1 is created"

fi    


# make a folder called folder2
if [ -d $folder2 ]; then
    echo "The folder named $folder2 already exists"

else
    mkdir $folder2
    echo "Folder with the name $folder2 is created"

fi


# make a folder called folder3

if [ -d $folder3 ]; then
    echo "The folder named $folder3 already exists"

else
    mkdir $folder3
    echo "Folder with the name $folder3 is created"

fi

cd $folder1

subfolder1="subfolder1"
subfolder2="subfolder2"
subfolder3="subfolder3"


# make a folder in folder 1 called subfolder1
if [ -d $subfolder1 ]; then
    echo "The folder named $subfolder1 already exists"

else
    mkdir $subfolder1
    echo "Folder with the name $subfolder1 is created"

fi    


# make a folder in folder 1 called subfolder2
if [ -d $subfolder2 ]; then
    echo "The folder named $subfolder2 already exists"

else
    mkdir $subfolder2
    echo "Folder with the name $subfolder2 is created"

fi


# make a folder in folder 1 called subfolder3
if [ -d $subfolder3 ]; then
    echo "The folder named $subfolder3 already exists"

else
    mkdir $subfolder3
    echo "Folder with the name $subfolder3 is created"

fi

# return to previous location

cd -

# delete folder 2 and 3

if [ -d $folder2 ]; then
    rm -r $folder2

else
    echo "The folder named $folder2 does not exist"

fi


if [ -d $folder3 ]; then
    rm -r $folder3

else
    echo "The folder named $folder3 does not exist"

fi




