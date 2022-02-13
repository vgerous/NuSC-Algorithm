from os import system
import time
import sys
import os
import subprocess
import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import STDOUT, check_output
import subprocess, threading

def RunSeedV3(seed, data_index, solver, dataname):
    if solver == 'domsat':
        command = "./domsat/domsat/DomSAT benchmark/" + dataname + "/" + str(data_index) + " 1000 > result/" + solver + "/" + dataname + "/" + str(data_index) + "_seed_" + str(seed)
    elif solver == 'wcc':
        command = "./wscp_new/wscp_new/Dist benchmark/" + dataname + "/" + str(data_index) + " 1 " + str(seed) + " 1000 > result/" + solver + "/" + dataname + "/" + str(data_index) + "_seed_" + str(seed)
    cmd = command
    os.system(cmd)

if __name__ == '__main__':
    seed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rail = ['rail507.txt.standard.txt', 'rail516.txt.standard.txt', 'rail582.txt.standard.txt', 'rail2536.txt.standard.txt', 'rail2586.txt.standard.txt', 'rail4284.txt.standard.txt', 'rail4872.txt.standard.txt']
    scpc = ['scpclr10.txt', 'scpclr11.txt', 'scpclr12.txt', 'scpclr13.txt', 'scpcyc06.txt', 'scpcyc07.txt', 'scpcyc08.txt', 'scpcyc09.txt', 'scpcyc10.txt', 'scpcyc11.txt']
    sts = ['sts135.txt', 'sts243.txt', 'sts405.txt', 'sts729.txt']
    scp = ['scp41.txt', 'scp42.txt', 'scp43.txt', 'scp44.txt', 'scp45.txt', 'scp46.txt', 'scp47.txt', 'scp48.txt', 'scp49.txt', 'scp51.txt', 'scp52.txt', 'scp53.txt', 'scp54.txt', 'scp55.txt', 'scp56.txt', 
        'scp57.txt', 'scp58.txt', 'scp59.txt', 'scp61.txt', 'scp62.txt', 'scp63.txt', 'scp64.txt', 'scp65.txt', 'scp410.txt', 'scp510.txt', 'scpa1.txt', 'scpa2.txt', 'scpa3.txt', 'scpa4.txt', 'scpa5.txt', 
        'scpb1.txt', 'scpb2.txt', 'scpb3.txt', 'scpb4.txt', 'scpb5.txt', 'scpc1.txt', 'scpc2.txt', 'scpc3.txt', 'scpc4.txt', 'scpc5.txt', 'scpd1.txt', 'scpd2.txt', 'scpd3.txt', 'scpd4.txt', 'scpd5.txt',
        'scpe1.txt', 'scpe2.txt', 'scpe3.txt', 'scpe4.txt', 'scpe5.txt', 'scpnre1.txt', 'scpnre2.txt', 'scpnre3.txt', 'scpnre4.txt', 'scpnre5.txt', 'scpnrf1.txt', 'scpnrf2.txt', 'scpnrf3.txt', 'scpnrf4.txt', 'scpnrf5.txt',
        'scpnrg1.txt', 'scpnrg2.txt', 'scpnrg3.txt', 'scpnrg4.txt', 'scpnrg5.txt', 'scpnrh1.txt', 'scpnrh2.txt', 'scpnrh3.txt', 'scpnrh4.txt', 'scpnrh5.txt']

    solver = str(sys.argv[1])
    dataname = str(sys.argv[2])

    if dataname == 'STS':
        dataset = sts
    elif dataname == 'SCPC':
        dataset = scpc
    elif dataname == 'rail':
        dataset = rail
    elif dataname == 'SCP':
        dataset = scp

    for cur_index in dataset:
        partial_RunSeed = partial(RunSeedV3, data_index = cur_index, solver = solver, dataname = dataname)
        with Pool(10) as p:
            print(p.map(partial_RunSeed, seed))
