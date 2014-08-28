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

import friday_harbor.experiment as experiment

# Point this to your data directory:
data_dir = '../friday_harbor/data' 

def test_wildtype_count():
    experiment_manager = experiment.ExperimentManager(data_dir=data_dir)
    assert len([e for e in experiment_manager.experiment_list if e.wildtype==True]) == 469
    print 'Wiltype count: %s' % 469
    

        
if __name__ == "__main__":
    test_wildtype_count()

