from examples.projcet01.manuever_object import ManueverObject
from pyjevsim import BehaviorModel, Infinite
import datetime

class Manuever(BehaviorModel):
    def __init__(self, name, platform, waypoints):
        BehaviorModel.__init__(self, name)
        
        self.platform: ManueverObject = platform
        self.waypoints = waypoints
        
        self.init_state("Wait")
        self.insert_state("Wait", Infinite)
        self.insert_state("Generate", 1)

        self.insert_input_port("start")

    def ext_trans(self,port, msg):
        if port == "start":
            print(f"{self.get_name()}[start_recv]: {datetime.datetime.now()}")
            self._cur_state = "Generate"

    def output(self, msg):
        # print(f"{self.get_name()}[Generate]: {datetime.datetime.now()}")
        x, y, z = self.platform.get_position()

        if not self.waypoints:
            self.platform.calc_next_pos_with_heading(1)

        else:
            distance = self.platform.calc_next_pos_with_pos(self.waypoints[0], 1)
            print(distance)
            if distance < 0.5:
                print(f'target position reached')
                # waypoints에서 현재 waypoint를 제거
                self.waypoints.pop(0)

        print(f'{x}, {y}, {z}: {datetime.datetime.now()}')
        return None
        
    def int_trans(self):
        if self._cur_state == "Generate":
            self._cur_state = "Generate"