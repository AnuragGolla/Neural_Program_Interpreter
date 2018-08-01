# coding: utf-8
import os
import pickle

from src.npi.bubblesort.config import FIELD_ROW, FIELD_WIDTH, FIELD_DEPTH
from src.npi.bubblesort.lib import BubblesortEnv, BubblesortProgramSet, BubblesortTeacher, create_char_map, create_questions, run_npi
from src.npi.bubblesort.model import BubblesortNPIModel
from src.npi.core import ResultLogger, RuntimeSystem
from src.npi.terminal_core import TerminalNPIRunner, Terminal



def main(filename: str, model_path: str):
    system = RuntimeSystem()
    program_set = BubblesortProgramSet()

    with open(filename, 'rb') as f:
        steps_list = pickle.load(f)

    npi_model = BubblesortNPIModel(system, model_path, program_set)
    npi_model.fit(steps_list)


if __name__ == '__main__':
    import sys
    DEBUG_MODE = os.environ.get('DEBUG')
    train_filename = sys.argv[1]
    model_output = sys.argv[2]
    main(train_filename, model_output)

