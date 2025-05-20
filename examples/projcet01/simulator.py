import project_config
from generator import Generator
from pyjevsim import SysExecutor, ExecutionType

se = SysExecutor(1, ex_mode=ExecutionType.R_TIME)
se.insert_input_port("start")

gen1 = Generator("Gen1", 1)
gen2 = Generator("Gen2", 2)

se.register_entity(gen1)
se.coupling_relation(se, "start", gen1, "start")

se.register_entity(gen2)
se.coupling_relation(se, "start", gen2, "start")

se.insert_external_event("start", None)

for _ in range(30):
	se.simulate(1)
	
se.terminate_simulation()