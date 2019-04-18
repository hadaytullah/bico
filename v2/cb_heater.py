from cb_base import CbBase

class CbHeater(CbBase):
    """A computational bacterium producing heat a.k.a heater
    """
    def __init__(self, env, name, context, event_stream, event_kinds, period, output):

        super().__init__(env, name, context, event_stream, event_kinds, period)

        #Heater properties
        self.heat_output = output
        self.heat_on = False
        self.output_unit = "watts"

    def sustenance_activity(self):
        if (self.heat_on):
            print ("{} at {} producing heat: {} {}".format(self.name,self.env.now,self.heat_output,self.output_unit))
        else:
            print ("{} at {} not producing heat".format(self.name,self.env.now))

    def on_interrupt_activity(self):
        print('{} at {} interrupted with {}'.format(self.name,self.env.now,self.event))
        if self.event[0] == 'heat_on' and not self.heat_on:
            self.heat_on = True
        elif self.event[0] == 'heat_off' and self.heat_on:
            self.heat_on = False
    
