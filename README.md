# pyPDF_split
Split PDFs with multiple student records into individual PDFs.

pyPDF_split searches a PDF for the string `StudentID:NNNNNNN` and splits the PDF into individual PDFs in a sub-folder with the StudentID embedded in the new file name.

pyPDF_split pairs nicely with the [insertFiles](https://github.com/txoof/insertFiles) and [create_folders](https://github.com/txoof/portfolioCreator) scripts.

Contact Information:
aaron.ciuffo@gmail.com


## Quick Start
**NOTE:** If this is the first time you've run this program, please see the [full instructions](#FullInstructions) below.


<a name='FullInstructions'></a>
## Full Instructions
1. Download pyPDF_split [here] ADD URL
2. Locate the downloaded file

![image.png](attachment:image.png)


```python
!jupyter-nbconvert --to markdown README.ipynb --stdout >> README.md
```

    [NbConvertApp] Converting notebook README.ipynb to markdown

