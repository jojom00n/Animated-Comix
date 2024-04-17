from ComixUtils import*


class Keyframes:
     keyframes = {
        0: ElementTransform(0, 1, 1), # rotate, scale, translateZ соответственно
        100: ElementTransform(0, 1, 1)
     }
     

     def __init__(self, transformZ_default):
         self.keyframes[0] = transformZ_default
         self.keyframes[100] = transformZ_default

     def set_frame(self, percent, transform):
        self.keyframes[percent] = transform

     def delete_frame(self, percent):
        del self.keyframes[percent]

     def sort_frames(self):
         sorted_dict = dict(sorted(self.keyframes.items))
         self.keyframes.clear()
         self.keyframes = sorted_dict
    

class Animation: 
    _animation_name = "none"
    _animation_duration = 0
    _animation_timing_function = "ease"
    _animation_delay = 0
    _animation_iteration_count = "1"
    _animation_direction = "normal"
    _animation_fill_mode = "none"
    _animation_play_state = "running"
    _keyframes = Keyframes(ElementTransform(1, 0, 1))


    def __init__(self, name, dur=0):
        self._animation_name = name
        self._animation_duration = dur

    def get_name(self):
        return self._animation_name
    
    def get_duration(self):
        return self._animation_duration
    
    def get_timing_fuction(self):
        return self._animation_timing_function
    
    def get_delay(self):
        return self._animation_delay
    
    def get_iteration_count(self):
        return self._animation_iteration_count
    
    def get_direction(self):
        return self._animation_direction
    
    def get_fill_mode(self):
        return self._animation_fill_mode
    
    def get_play_state(self):
        return self._animation_play_state
    



    def set_name(self, name):
        self._animation_name = name
    
    def set_duration(self, dur):
        self._animation_duration = dur
    
    def set_timing_fuction(self, timing_f):
        self._animation_timing_function = timing_f
    
    def set_delay(self, delay):
        self._animation_delay = delay
    
    def set_iteration_count(self, iter_count):
        self._animation_iteration_count = iter_count
    
    def set_direction(self, dir):
        self._animation_direction = dir
    
    def set_fill_mode(self, fill_md):
        self._animation_fill_mode = fill_md
    
    def set_play_state(self, play_st):
        self._animation_play_state = play_st
  