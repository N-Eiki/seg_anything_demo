import cv2  # type: ignore

from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
from segment_anything import sam_model_registry, SamPredictor

import argparse
import json
import os
from typing import Any, Dict, List
import time
import numpy as np

from parser import get_amg_kwargs

class InferBot:
    def __init__(self, args):
        print("Loading model...")
        sam = sam_model_registry['default'](checkpoint=args.checkpoint)
        sam.to(device=args.device)
        self.predictor = SamPredictor(sam)
        
    def forward(self, image_path, input_point, input_label):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        self.predictor.set_image(image)
        masks, scores, logits = self.predictor.predict(
                point_coords=input_point,
                point_labels=input_label,
                multimask_output=True,
        )
        mask = masks[0]
        image[:,:,0][mask.astype(bool)] = 0
        return image
        
