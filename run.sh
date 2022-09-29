#!/bin/bash
cd "${0%/*}/repositories/stable-diffusion"
apt-get update && apt-get install wget
wget https://raw.githubusercontent.com/juankysoriano/dr-dream/main/dr-dream.py
wget https://raw.githubusercontent.com/juankysoriano/dr-dream/main/requirements.txt

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
nvm install 12
nvm use 12
npm install -g localtunnel
pip install -r requirements.txt
pip install -e .
pip install taming-transformers-rom1504
mkdir ./models/ldm/stable-diffusion-v1/
cp ../../model.ckpt ./models/ldm/stable-diffusion-v1/

python dr-dream.py & lt --port 8000 --subdomain dr-dream 
