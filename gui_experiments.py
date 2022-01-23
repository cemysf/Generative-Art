"""
@author: cemysf
"""

from abc import ABC, abstractclassmethod
from functools import partial
import random 

from examples import draw_flow_field, draw_delta_body, draw_white_noise, draw_perlin, draw_vectors, draw_perlin_rounding


class ArtFuncExperiment(ABC):
    @abstractclassmethod
    def use(cls, width, height):
        """ usage: specialize use function for different types of art functions"""
        raise NotImplementedError("Implement this on child class")


class FlowField(ArtFuncExperiment):
    # default params
    FUNC_KWARGS = dict(n_x=2,n_y=2,step=0.001)
    FUNC_TO_USE = partial(draw_flow_field)

    @classmethod
    def use(cls, width, height):
        """ common across all FlowField functions"""
        return cls.FUNC_TO_USE(width, height, seed=random.randint(0, 100000000), color=random.randint(0,360), **cls.FUNC_KWARGS)


class FlowFieldSimple(FlowField):
    """ Original values, simple flow image """
    pass


class FlowFieldCurvy(FlowField):
    """ More curve """
    FUNC_KWARGS = dict(n_x=8,n_y=8,step=0.002)
    FUNC_TO_USE = partial(draw_flow_field)


class FlowFieldStringArt(FlowField):
    """ Looks like string art """
    FUNC_KWARGS = dict(n_x=4,n_y=5,step=0.35)
    FUNC_TO_USE = partial(draw_flow_field)



FUNCTION_IN_USE = FlowFieldStringArt
