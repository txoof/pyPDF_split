#!/bin/bash
appname="pyPDF_split"
appdir="./pyPDF_split"
build_log="../build.log"
pushd $appdir

pipenv run pyinstaller --onefile --noconfirm --clean --exclude-module IPython $appname.py > $build_log 2>&1

if [ $? == 0 ]; then
  echo "successfully built $appname"
else
  echo "build failed -- see `basename $build_log`"
  popd
  exit 1
fi

#echo "creating archive"
#pushd ./dist
#tar cvzf ../../$appname.tgz ./$appname
~/bin/develtools/codesign.py ./pyPDF.ini

#popd
popd

echo "run: $ git commit -am 'update build'" 
echo "$ git push"
echo "remember to push to github"

