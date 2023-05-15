# Modified by Aslan Satary Dizaji, Copyright (c) 2022.

# Copyright (c) 2020, salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root
# or https://opensource.org/licenses/BSD-3-Clause

from modified_ai_economist.foundation.base.base_env import scenario_registry

from .one_step_economy import one_step_economy

from .simple_wood_and_stone_and_iron import (
    dynamic_layout,
    layout_from_file,
    vote_and_invest_scenario,
    rule_of_law_or_arbitrary_government_scenario,
)

# Import files that add Scenario class(es) to scenario_registry
# -------------------------------------------------------------