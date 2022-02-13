# NuSC
- An Effective Local Search Algorithm for Solving the Set Covering Problem


## 1. Set up
#### 1. Set a conda virtual environment
```bash
conda create -n NuSC python=3.7 anaconda --yes
```

#### 2. Clone the repository
```bash
git clone https://github.com/vgerous/NuSC-Algorithm.git
```

#### 3. Install required packages
```bash
conda activate NuSC
conda install --file requirements.txt
```



## 1. Run NuSC
#### 1. Run binary file
NuSC algorithm can be run with binary file: **NuSC-algorithm/NuSC/NuSC**
##### Example (Run NuSC on rail benchmark)
```
./NuSC/NuSC  <dataset> <time limits> <seed> <score-weight> <tabu-size> <novelty> 
```
```bash
./NuSC/NuSC benchmark/rail/rail516.txt.standard.txt 1000 1 5 4 0.3 > results/rail/rail516.txt.standard.txt_with_seed_1.out
```

#### 2. Run script
NuSC algorithm can be run with script: **NuSC-algorithm/run_mysolver.py**

##### Example (Run NuSC on rail benchmark)
```bash
python NuSC/run_mysolver.py rail
```

## 2. Run Competitors
#### 1. Max-SAT solvers
All Max-SAT solvers can be run in the file **maxsat-evaluations-2021/runsolver_maxsat.py**

##### Example (Run loandra on rail benchmark)
```bash
python maxsat-evaluations-2021/runsolver_maxsat.py loandra rail
```

#### 2. SCP solvers
All SCP solvers can be run in the file **set-cover-competitors/runsolver_scp.py**

##### Example (Run domsat on rail benchmark)
```bash
python set-cover-competitors/runsolver_scp.py domsat rail
```

## 3. Output
The output file of our solver consists of the solution searching path. A typical output file make looks like:

```bash
o 181 0.14

o 180 0.21

v 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 ......
```
The notation 'o' means the recorded solution path followed with objective value (e.g. 180) and the time this solution was found (in seconds, e.g. 0.21).

The notation 'v' followed with the allocation result.
