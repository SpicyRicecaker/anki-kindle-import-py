## running
```shell
virtualenv venv
# replace venv/bin/activate with venv/bin/activate.nu
rm venv/bin/activate
mv venv/bin/activate.nu venv/bin/activate
# load virtualenv
source venv/bin/activate
# install everything
pip install requirements.txt
```