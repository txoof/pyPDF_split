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


## Quick Start
**NOTE:** If this is the first time you've run this program, please see the [full instructions](#FullInstructions) below.

#### [Download link](https://github.com/txoof/pyPDF_split/blob/master/pypdfsplit.pkg)

1. Launch the `py_pdfsplit` application from your `Applications` folder by double clicking on it.
2. When prompted, locate a PDF that needs to be split by clicking on the `Browse` button -- this will launch a Finder window allowing you find and choose a single PDF file
    ![GUI Browse Image](./docs/gui_browse.png)
3. Click `Ok` when ready
4. pyPDF_split will split the PDF into a sub-folder within the same folder as the original pdf:
    ![Output folder with split pdfs](./docs/output_split.png)
5. Split another PDF by clicking `Browse` or `Cancel` to quit

<a name='FullInstructions'></a>
## Full Instructions
1. Download the latest version of pyPDF_split [here](https://github.com/txoof/pyPDF_split/blob/master/pypdfsplit.pkg)
2. Locate the downloaded file in the Downloads folder and double click on the `.zip` file to extract it
3. Right click on the pyPDF_Split and choose "Open" in the following dialogue choose "Open" again - Note you may have to do this TWICE.
   - ![Open Dialogue](./docs/open_dialogue.png)

4. After approving the application, drag it into the `Applications` Folder.
5. Double click on the pyPDF_Split application to launch it
6. When prompted, locate a PDF that needs to be split by clicking on the `Browse` button -- this will launch a Finder window allowing you find and choose a single PDF file
    ![GUI Browse Image](./docs/gui_browse.png)
7. Click `Ok` when ready
8. pyPDF_split will split the PDF into a sub-folder within the same folder as the original pdf:
    ![Output folder with split pdfs](./docs/output_split.png)
9. Split another PDF by clicking `Browse` or `Cancel` to quit

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