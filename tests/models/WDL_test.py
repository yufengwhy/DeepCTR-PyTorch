# -*- coding: utf-8 -*-
import pytest
import sys
sys.path.append('/data/tangj/code/deepctr/DeepCTR-PyTorch/tests')
from deepctr_torch.models import WDL
from utils import get_test_data, SAMPLE_SIZE, check_model

@pytest.mark.parametrize(
    'sparse_feature_num,dense_feature_num',
    [(2, 0), (0, 2)#,(2, 2)
     ]
)
def test_WDL(sparse_feature_num, dense_feature_num):
    model_name = "WDL"
    sample_size = SAMPLE_SIZE
    x, y, feature_columns = get_test_data(
        sample_size, sparse_feature_num, dense_feature_num)

    model = WDL(feature_columns, feature_columns,
                dnn_hidden_units=[32, 32], dnn_dropout=0.5)
    check_model(model, model_name, x, y)


if __name__ == "__main__":
    # test_WDL(0, 2)
    pass