#!/bin/bash
xhost +
# /opt/X11/bin/xhost +

docker run -it --privileged\
    -m 15g\
    --env="DISPLAY=host.docker.internal:0" \
    -v $HOME/.Xauthority:/root/.Xauthority \
    -v /Users/n.eiki/source/poetry_seg_anything/mnt_workdir:/mnt\
    -v /Users/n.eiki/source/poetry_seg_anything/segment-anything/:/workdir/poetry_seg_anything/segment-anything \
    --name seg_anything poetry_docker_py38 bash 

#   poetry run python scripts/amg.py --checkpoint /mnt/ckpt/sam_vit_h_4b8939.pth --model-type default --input /mnt/imgs/ノビル.jpg --output /mnt/output/

# import matplotlib.pyplot as plt;plt.plot([0, 1, 2]);plt.show()