
Setting up the environment:

```
brew install swig
python3 -m venv .venv
source .venv/bin/activate
cd .venv
git clone --recursive https://github.com/bambocher/pocketsphinx-python
cd pocketsphinx-python
sed -i 's/<al.h>/<OpenAL/al.h>/g' pocketsphinx-python/deps/sphinxbase/src/libsphinxad/ad_openal.c
sed -i 's/<alc.h>/<OpenAL/alc.h>/g' pocketsphinx-python/deps/sphinxbase/src/libsphinxad/ad_openal.c
git pull --recurse-submodules
pip3 install -r requirements.txt
```

```
git clone --recursive https://github.com/bambocher/pocketsphinx-python

sed -i 's/<al.h>/<OpenAL/al.h>/g' pocketsphinx-python/deps/sphinxbase/src/libsphinxad/ad_openal.c
sed -i 's/<alc.h>/<OpenAL/alc.h>/g' pocketsphinx-python/deps/sphinxbase/src/libsphinxad/ad_openal.c
```