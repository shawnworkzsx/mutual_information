import numpy as np
#compute discrete mutual information
def MI(p00, p01, p10, p11, px0, px1, py0, py1):
    if p00 == 0:
        part1 = 0
    if p01 == 0:
        part2 = 0
    if p10 == 0:
        part3 = 0
    if p11 == 0:
        part4 = 0
    if p00 != 0:
        part1 = p00 * (np.log2((p00) / (px0 * py0)))
    if p01 != 0:
        part2 = p01 * np.log2((p01) / (px0 * py1))
    if p10 != 0:
        part3 = p10 * np.log2((p10) / (px1 * py0))
    if p11 != 0:
        part4 = p11 * np.log2((p11) / (px1 * py1))

    res = part1 + part2 + part3 + part4
    res = res.round(4)
    if res == -0.0:
        res = 0.0
    return res