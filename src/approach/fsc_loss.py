import math
import numpy as np
import torch
import torch.nn as nn
from .utils import *
from torch.distributions import Normal, Independent
from torch import distributed as dist

class CalibrationClass(nn.Module):

    def __init__(self, coef_2i=0.1):
        super(CalibrationClass, self).__init__()
        self.eps = 1e-8
        self.coef_2i = coef_2i

    def forward(self, x, x_label, uniq_l, y, i):
        #Sec.3.2 inter-class learning
        loss1=0.0
        if len(uniq_l)-1>i:
            x_label2 = x[y==uniq_l[i+1],:]
            len_x_label= len(x_label)
            len_x_label2= len(x_label2)             
            min_len = min(len_x_label, len_x_label2)
            x_diff =x_label[:min_len,:]-  x_label2[:min_len,:]
            loss1=(1+self.eps)/(x_diff.pow(2).mean())
        #Sec.3.2 intra-class learning
        m = nn.MaxPool1d(32,stride=16)
        m2 = m(x_label.unsqueeze(1)).squeeze()
        loss2 = 0.0
        if len(m2)>2:
            for aa in range(len(m2)-1):
                loss2+=(m2[aa,:]-m2[aa+1,:]).pow(2).mean() 
        fsc_loss =  self.coef_2i*(loss1+loss2) 
        return fsc_loss 
