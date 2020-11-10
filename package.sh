#!/bin/bash
pkgname=pypdfsplit.pkg
pycodesign.py pycodesign.ini 

git commit -m "repackage, sign, notarize $pkgname"
