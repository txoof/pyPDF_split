#!/usr/bin/env python3
# coding: utf-8




import re
import sys
from pathlib import Path

import os.path
import PyPDF2
import pdfminer
import pdfplumber
import PySimpleGUI as sg

import constants

import logging






logger = logging.getLogger('pypdf_splitter')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)








class PyPDFSplitter:
    # contributed by picobas
    def get_breaks(file):
        file = Path(file).expanduser().absolute()

        try:
            source_pdf = pdfplumber.open(file);
        except (FileNotFoundError, pdfminer.pdfparser.PDFSyntaxError, IsADirectoryError) as e:
            logger.error(f'Failed to read source pdf: {e}')
            return []

        page_breaks = []

        last_record = {'id': None, 'pages': []}

        for page in range(0, len(source_pdf.pages)):
            this_record = ({'id': None, 'pages': []})
            text = source_pdf.pages[page].extract_text()
            student_number = re.search('student\W?id:\W?(\d{6})', text, re.IGNORECASE)

            if student_number:
                logger.debug(f"Found student: {student_number.group(1)}")
                page_breaks.append(last_record)
                this_record['id'] = student_number.group(1)
                this_record['pages'].append(page)
                last_record = this_record

            else:
                last_record['pages'].append(page)

        return page_breaks

    def split_pdf(file, page_breaks):
        file = Path(file).expanduser().absolute()
        file_name = os.path.splitext(file.name)[0]
        dest_path = file.parent / f'{file_name}_split'

        output = {}

        try:
            source_pdf = PyPDF2.PdfFileReader(str(file))
        except (FileNotFoundError, PyPDF2.utils.PdfReadError, IsADirectoryError) as e:
            logger.error(f'Failed to split source pdf: {e}')
            return False

        for record in page_breaks:
            output_path = 'Failed'
            if not record['id']:
                continue
            pdf_writer = PyPDF2.PdfFileWriter()
            for page in record['pages']:
                try:
                    pdf_writer.addPage(source_pdf.getPage(page))
                except Exception as e:
                    logger.error(f'failed to add page: "{page}" for record: "{record}" error: {e}')

            try:
                output_path = dest_path / f'{record["id"]} - {file_name}.pdf'
                output_path.parent.mkdir(exist_ok=True)
                with open(str(output_path), "wb") as dest_file:
                    pdf_writer.write(dest_file)

            except Exception as e:
                logger.error(f'error outputing pdf: {e}')
                output_path = f'Failed outputing pdf: {e}'
                pass
            finally:
                output[record['id']] = output_path
        return output






def main():
    interactive = False

    if (len(sys.argv) == 1) or ('-f' in sys.argv):
        interactive = True
    else:
        fname = sys.argv[1]

    while interactive:
        logger.debug('prompt user for PDF file')
        fname = sg.popup_get_file(f'v{constants.version}: Choose a PDF to split')
        logger.debug(f'fname returned: {fname}')
        if fname in [None, ]:
            logger.info('user canceled')
            break
        if fname:
            breaks = PyPDFSplitter.get_breaks(fname)
            output = PyPDFSplitter.split_pdf(fname, breaks)

        if output:
            ## add a popup that summarizes what was done
            strings = f'{len(output)} records extracted -- see below for full output\n'
            strings = strings + 'split records are placed in the same directory as the original PDF\n\n\n'
            strings = strings + str(output)
            sg.popup_scrolled(strings,
                              title='Processed files',
                              keep_on_top=True,
                              size=(80, 50))
        else:
            sg.popup('Cancel', "No PDF supplied")






if __name__ == "__main__":
    main()









