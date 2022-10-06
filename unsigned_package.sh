#!/bin/bash
source_path=./pyPDF_split/dist/pyPDF_split
package_name="pypdfsplit"
arch=$(uname -p)
zipfilename="$package_name-unsigned-$arch.zip"

zip -r $zipfilename $source_path

echo created $zipfilename
echo remember to push to git repo
