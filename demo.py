import numpy as np

if __name__ == "__main__":
    a = np.load("logs/magicpoint_synth_homoAdapt_coco/predictions/train/000000000009.npz")
    print(a["pts"], a["pts"].shape)
    b = np.load("logs/magicpoint_synth_homoAdapt_coco/predictions/train/000000000025.npz")
    print(b["pts"], b["pts"].shape)