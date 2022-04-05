{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c750c84b",
   "metadata": {},
   "source": [
    "# Assignment 10 Solutions"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c00ae223",
   "metadata": {},
   "source": [
    "#### 1. How do you distinguish between shutil.copy() and shutil.copytree()?\n",
    "**Ans:** `shutil.copy()` method is used to copy the contents of a file from one file to another file/folder, it primary takes two arguments `src`,`dest`, `src` represents the file to be copied where as destination refers to the file/folder to where the `src` data should be copied, if `dest` is a folder name the `src` with exact name will be copied to the `dest` folder, if its a file then the contents of `src` will be copied to `dest` where `dest` retains it name.\n",
    "\n",
    "`shutil.copytree()` function is used to copy the entire contents of a folder to other folder. it also takes two arguments `src` & `dest`, it copies all the content recursively and stores it in `dest`. the important catch here is `dest` must not exist prior to this and it will be created during the copy operation. Permissions and times of directories are copied with `shutil.copystat()` and individual files are copied using `shutil.copy2()` by default which can be modified using `copy_function` attribute.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a932861",
   "metadata": {},
   "source": [
    "#### 2. What function is used to rename files??\n",
    "**Ans:** `os.rename()` function is used to rename files or directories using a python program, this function takes two arguments `src` and `dest`, `src` represents the name file/directory which we want to rename, whereas `dest` represents the new name of the file/directory."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34ce7a3d",
   "metadata": {},
   "source": [
    "#### 3. What is the difference between the delete functions in the send2trash and shutil modules?\n",
    "**Ans:** Shutil module provides a funciton called as `shutil.rmtree()` which deletes a directory and all its contents. The other functions with similar functionality are `os.remove()` -> removes a file, `os.rmdir()` removes a empty directory. The problem with these functions is once a file is deleted. it will be lost permanently, if a file is deleted accidentally using these methods there is no way we can recover the deleted file\n",
    "\n",
    "Where as send2trash module provides a function called `send2trash.send2trash()` to delete a file/directory. these methods moves the files/directories to trash folder instead of permanently deleting them. hence if a file/folder is deleted accidentally it can be still recovered from trash folder, if is deleted using the `send2trash.send2trash()` function. `send2trash` is not included with python standard libary like `os` & `shutil` modules. it needs to be installed explicitly using the command `!pip install send2trash`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf6ed792",
   "metadata": {},
   "source": [
    "#### 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?\n",
    "**Ans:** ZipFile Module provides a method called as `zipfile.ZipFile()` to read and write to zipFiles. it takes arugments lile filename and mode etc `zipfile.ZipFile('filename', mode = 'r')`"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c625fcea",
   "metadata": {},
   "source": [
    "#### 5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4710d7d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Folder Name ➞ C:\\Users\\vishnu.adepu\\Documents\\iNeuron-Assignments\\Python Basic Assignment\\Dummy Source\n",
      "\n",
      "Sub Folders ➞ []\n",
      "\n",
      "Files ➞ ['01.Assignment_01.ipynb', '02.Assignment_02.ipynb', '03.Assignment_03.ipynb', '04.Assignment_04.ipynb', '05.Assignment_05.ipynb', '06.Assignment_06.ipynb', '07.Assignment_07.ipynb', '08.Assignment_08.ipynb', '09.Assignment_09.ipynb', '10.Assignment_10.ipynb', '11.Assignment_11.ipynb', '12.Assignment_12.ipynb', '13.Assignment_13.ipynb', '14.Assignment_14.ipynb', '15.Assignment_15.ipynb', '16.Assignment_16.ipynb', '17.Assignment_17.ipynb', '18.Assignment_18.ipynb', '19.Assignment_19.ipynb', '20.Assignment_20.ipynb', '21.Assignment_21.ipynb', '22.Assignment_22.ipynb', '23.Assignment_23.ipynb', '24.Assignment_24.ipynb', '25.Assignment_25.ipynb']\n",
      "\n",
      "Files copied successfully from C:\\Users\\vishnu.adepu\\Documents\\iNeuron-Assignments\\Python Basic Assignment\\Dummy Source to C:\\Users\\vishnu.adepu\\Documents\\iNeuron-Assignments\\Python Basic Assignment\\Dummy Destination\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "\n",
    "def search_and_copy(source,destination,extensions):\n",
    "    source = os.path.abspath(source)\n",
    "    destination = os.path.abspath(destination)\n",
    "    for foldername, subfolder, filenames in os.walk(source):\n",
    "        print(f'Folder Name ➞ {foldername}',end='\\n\\n')\n",
    "        print(f'Sub Folders ➞ {subfolder}',end='\\n\\n')\n",
    "        print(f'Files ➞ {filenames}',end='\\n\\n')\n",
    "        for filename in filenames:\n",
    "            fileName,extension = os.path.splitext(filename)\n",
    "            if extension in extensions:\n",
    "                targetFile = foldername+os.path.sep+fileName+extension\n",
    "                shutil.copy(targetFile, destination)\n",
    "        print(f'Files copied successfully from {source} to {destination}')\n",
    "    \n",
    "extensions = ['.pdf','.jpg','.ipynb']\n",
    "source = 'Dummy Source'\n",
    "destination = 'Dummy Destination'\n",
    "search_and_copy(source, destination, extensions)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
