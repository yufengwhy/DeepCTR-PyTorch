# -*- coding: utf-8 -*-
import pytest
import sys
sys.path.append('/data/tangj/code/deepctr/DeepCTR-PyTorch/tests')
from deepctr_torch.models import AFM
from utils import get_test_data, SAMPLE_SIZE, check_model

@pytest.mark.parametrize(
    'use_attention, sparse_feature_num, dense_feature_num',
    [(True, 3, 0),]
)

def test_AFM(use_attention, sparse_feature_num, dense_feature_num):
    model_name = 'AFM'
    sample_size = SAMPLE_SIZE
    x, y, feature_columns = get_test_data(sample_size, sparse_feature_num, dense_feature_num)
    print('xxxxx', feature_columns)
    model = AFM(feature_columns, feature_columns, use_attention=use_attention, afm_dropout=0.5)

    check_model(model, model_name, x, y)

if __name__ == '__main__':
    pass