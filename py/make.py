import os
import yaml

from modules.sd_models import checkpoints_list

def make_yaml():
    y = {}
    for k in checkpoints_list.keys():
        y[checkpoints_list[k].model_name] = {
            'description': k,
            'weights': checkpoints_list[k].filename,
            'config': 'configs/stable-diffusion/v1-inference.yaml',
            'width': 512,
            'height': 512,
        }
        # 1111のデフォルトのconfig値は使わない
        cfg = os.path.splitext(checkpoints_list[k].filename)[0] + '.yaml'
        if os.path.exists(cfg):
            y[checkpoints_list[k].model_name]['config'] = cfg
        vae = os.path.splitext(checkpoints_list[k].filename)[0] + '.vae.pt'
        if os.path.exists(vae):
            y[checkpoints_list[k].model_name]['vae'] = vae

    return yaml.dump(y)
