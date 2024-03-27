from PaddleTools.GAN import FOM
import argparse
from config import Config

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='default.yaml', help='config file')

if __name__ == '__main__':
    args = parser.parse_args()
    _Config = Config(args.config)
    GAN_Config = _Config.GAN()

    cvh = FOM(GAN_Config['FOM_INPUT_IMAGE'],GAN_Config['FOM_DRIVING_VIDEO'],GAN_Config['FOM_OUTPUT_VIDEO'])

    print('The virtual person has been successfully created at {}'.format(cvh))
