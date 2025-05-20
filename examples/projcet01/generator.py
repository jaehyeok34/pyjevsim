from pyjevsim import BehaviorModel, Infinite
import datetime

class Generator(BehaviorModel):
    # def __init__(self, name, platform):
    def __init__(self, name, gen_freq):
        BehaviorModel.__init__(self, name)
        
        # self.platform = platform
        
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", gen_freq)

        self.insert_input_port("start")

    def ext_trans(self,port, msg):
        if port == "start":
            print(f"{self.get_name()}[start_recv]: {datetime.datetime.now()}")
            self._cur_state = "Generate"

    def output(self, msg):
        # self.platform.mo.calc_next_pos_with_heading(1)
        print(f"{self.get_name()}[Generate]: {datetime.datetime.now()}")
        return None
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"