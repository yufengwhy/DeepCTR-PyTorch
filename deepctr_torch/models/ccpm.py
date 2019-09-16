"""
Author:
    Abhilash Awasthi,maddy14awasthi@gmail.com
Reference:
    [1] Liu Q, Yu F, Wu S, et al. A convolutional click prediction model[C]//Proceedings of the 24th ACM International on Conference on Information and Knowledge Management. ACM, 2015: 1743-1746.
    (http://ir.ia.ac.cn/bitstream/173211/12337/1/A%20Convolutional%20Click%20Prediction%20Model.pdf)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from .basemodel import BaseModel

