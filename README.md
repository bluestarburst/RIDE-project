# RIDE-project
temporary name

### !!! IMPORTANT !!!

Please run the following commands to initialize and update the submodules

'''bash
git submodule init
git submodule update
'''


## Setup

0. (WINDOWS ONLY) Setup WSL (super useful for future projects trust me)
http://learn.microsoft.com/en-us/windows/wsl/install

1. Install dependencies and setup conda environment

```bash
./setup.sh
```

2. Download the SIM from https://github.com/tawnkramer/gym-donkeycar/releases

## (Optional) Create your own donkey car env (works for both physical and sim) *probably*

```bash
donkey createcar --path ./cars/<name-of-car>
```

For virtual donkey cars, you need to edit the myconfig.py file to connect to the donkey sim.

```bash
cd <name-of-car>
code myconfig.py
```

Please add the following to the bottom of the myconfig.py file:

```bash
DONKEY_GYM = True
DONKEY_SIM_PATH = "remote" 
DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0" 
GYM_CONF = { "body_style" : "donkey", "body_rgb" : (128, 128, 128), "car_name" : "<name-of-car>", "font_size" : 100}
SIM_HOST = "<IP Address>"              # when racing on virtual-race-league use host "trainmydonkey.com"
```

By default localhost on windows is not available to WSL, so you need to find your real IP address.

To find your IP address in WSL, run the following command:

```bash
ip route
```

The IP address to use is found in this line: `default via <IP Address>`

## Running the cars

1. Run the sim (downloaded earlier from https://github.com/tawnkramer/gym-donkeycar/releases)

2. Once running, select a course. It will appear empty for now.

3. Run the Donkey car

Be sure you are in the `donkey` conda environment!

| Type | Command |
|------|---------|
| Drive | `cd cars/<name-of-car> && python manage.py drive` |
| Train | `cd cars/<name-of-car> && donkey train --tub ./data --model models/<name-of-model>.h5` |
| Sim | `cd cars/<name-of-car> && python manage.py drive --model models/<name-of-model>.h5` |


All information for the donkey car is in 
- [Donkey Installation Docs](https://docs.donkeycar.com/guide/host_pc/setup_ubuntu/)
- [Donkey Gym Docs](https://docs.donkeycar.com/guide/deep_learning/simulator/)

---
---
---


# ~~Using sdsandbox 2025 (OLD)~~

1. Install Unity 2020.3.48f1 (via Unity Hub)

2. Create CONDA environment
```bash
conda create -n ride python=3.7
```
3. Install Tensorflow 1.15.5 (via pip) 
```bash
pip install tensorflow==1.15.5
```
4. Install other dependencies
```bash
cd sdsandbox
pip install -r requirements.txt
```
5. Open the unity project via Unity Hub (sdsim)
6. Open the scene (generated_road) in Assets/Scenes
7. Run the scene and click "NN Control over Network"
8. Run the prediction client
```bash
python predict_client.py --model=../outputs/mymodel.h5
```
(if running the on WSL)

Get the IP address of the machine
```bash
ip route
```

The IP address to use is default via <IP Address>

```bash
python predict_client.py --model=../outputs/mymodel.h5 --host=<IP Address> --port=9091
```
