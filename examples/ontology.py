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

from friday_harbor.ontology import Ontology

# Settings:
data_dir = '../friday_harbor/data'

# Construct the ontology from the data directory:
ontology = Ontology(data_dir=data_dir)

# Print data about each possible structure:
for s in ontology.structure_list:
    print s.name, s.structure_id, s.acronym

