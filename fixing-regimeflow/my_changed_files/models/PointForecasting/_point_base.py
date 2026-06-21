import os
import torch
import sys
import torch.nn as nn
sys.path.extend(['./', '../', '../../'])
from models import Nonstationary_Transformer, DLinear, \
    PatchTST, iTransformer, TimeMixer, TimeXer

# Lazy imports for optional dependencies
try:
    from models import S_Mamba
except Exception:
    S_Mamba = None

try:
    from models import BiMamba4TS
except Exception:
    BiMamba4TS = None

try:
    from models import Chronos
except Exception:
    Chronos = None


class _PointBaseModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model_dict = {
            'Nonstationary_Transformer': Nonstationary_Transformer,
            'DLinear': DLinear,
            'PatchTST': PatchTST,
            'iTransformer': iTransformer,
            'TimeMixer': TimeMixer,
            'TimeXer': TimeXer,
        }
        if S_Mamba is not None:
            self.model_dict['S_Mamba'] = S_Mamba
        if BiMamba4TS is not None:
            self.model_dict['BiMamba4TS'] = BiMamba4TS
        if Chronos is not None:
            self.model_dict['Chronos'] = Chronos
