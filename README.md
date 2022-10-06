# pyPDF_split
Split PDFs with multiple student records into individual PDFs.

If the pyPDF program is unavialble or does not work, see these [backup instructions](https://github.com/txoof/pyPDF_split/blob/master/Backup_Plan.md#backup-plan-for-pypdfsplit)

pyPDF_split searches a PDF for the string `StudentID:NNNNNNN` and splits the PDF into individual PDFs in a sub-folder with the StudentID embedded in the new file name.

pyPDF_split can handle student IDs in the following formats:

* `StudentID:123456`; `StudentId:123456`; `STUDENTID:123456`; `studentid:123456` 
    - upper/lower case is ignored in all cases
* `Student ID:123456`; `Student ID: 123456`

pyPDF_split pairs nicely with the [insertFiles](https://github.com/txoof/insertFiles) and [create_folders](https://github.com/txoof/portfolioCreator) scripts.

Contact Information:
aaron.ciuffo@gmail.com


## Instructions

### Download:

* [pyPDF Split for all macs](https://github.com/txoof/pyPDF_split/blob/master/pypdfsplit-unsigned-i386.zip)
* [pyPDF Split for ARM (newer Macs)](https://github.com/txoof/pyPDF_split/blob/master/pypdfsplit-unsigned-arm.zip)
 
## First Run

1. Unzip the zip file
2. Locate the pyPDF_split application in the newly unzipped folder and drag it into your `Applications` folder
3. Locate the pyPDF_split application in the `Applications` folder and **RIGHT CLICK** on the application. 
    - choose "Open". You may see several warning screens (see below), this is normal. Choose 'Open' each time
    - You may need to do this step at least two times.
    - ![Open Dialogue](./docs/open_dialogue.png)

## Splitting PDFs

1.  When prompted, locate a PDF that needs to be split by clicking on the `Browse` button -- this will launch a Finder window allowing you find and choose a single PDF file
    - ![GUI Browse Image](./docs/gui_browse.png)
5. Click `Ok` when ready
6. pyPDF_split will split the PDF into a sub-folder within the same folder as the original pdf:
    ![Output folder with split pdfs](./docs/output_split.png)
7. Split another PDF by clicking `Browse` or `Cancel` to quit



## Building pyPDF_Split

Build this script in a pyenv/pipenv with TK built in.
1. See [this Gist](https://gist.github.com/txoof/675e72d43f1bfbade04fdcec99ff4085) for complete instructions for setting up a working pyenv with TK, pipenv and Jupyter
2. Set up a Python 3+ jupyter kernel for further editing from within this repo directory:
```
$ pipenv --3 install ipykernel
$ projectName=$(basename `pipenv --venv`)
$ pipenv run python -m ipykernel install --user --name="${projectName}"
```
3. Make any edits needed and then rebuild the program with:
```
$ ./build.sh
```
4. The executable will be created in the `./dist/` folder.