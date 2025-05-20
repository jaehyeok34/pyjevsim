import project_config
from examples.projcet01.manuever import Manuever
from pyjevsim import SysExecutor, ExecutionType
from examples.projcet01.manuever_object import ManueverObject

waypoints = [(3, 3, 0), (10, 3, 0), (10, 0, 0), (0, 0, 0)]

mb1 = ManueverObject(0, 0, 0, 0, 1, 0)
# mb2 = ManueverObject(10, 0, 0, 0, 10, 0)

se = SysExecutor(1, ex_mode=ExecutionType.R_TIME)
se.insert_input_port("start")

gen1 = Manuever("Gen1", mb1, waypoints)
# gen2 = Manuever("Gen2", mb2)

se.register_entity(gen1)
# se.register_entity(gen2)

# 시뮬레이션 엔진과 모델 연결
se.coupling_relation(se, "start", gen1, "start")
# se.coupling_relation(se, "start", gen2, "start")

se.insert_external_event("start", None)

for _ in range(30):
	se.simulate(1)
	
se.terminate_simulation()