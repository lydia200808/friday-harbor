# Copyright 2014 Allen Institute for Brain Science
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Nicholas Cain
# Allen Institute for Brain Science
# June 11 2014
# nicholasc@alleninstitute.org

import json
import requests
import os
import sys
from friday_harbor.paths import Paths
from friday_harbor.data.api import experiment_search

def refresh_experiment_json(data_dir='.', injection_structures=None, wild=True, cre=True):

    paths = Paths(data_dir)

    experiment_data = experiment_search(injection_structures, wild, cre)

    # Write 
    with open(paths.experiment_json_file_name,'wb') as f:
        json.dump(experiment_data, f)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        refresh_experiment_json(sys.argv[1])
    else:
        refresh_experiment_json()
    





