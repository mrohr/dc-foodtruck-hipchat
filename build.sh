rm -rf out
mkdir -p out
cp -r src/* out/
cp config.json out/
cp -r venv/lib/python2.7/site-packages/* out/
touch out/__init__.py
rm out.zip
cd out && zip -r ../out.zip * && cd ..
