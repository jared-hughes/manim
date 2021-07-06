"""Mobjects representing implicit curves and surfaces."""

__all__ = ["ImplicitCurve"]

import numpy as np
from typing import Callable, Tuple

from ..mobject.types.vectorized_mobject import VMobject
from .opengl_compatibility import ConvertToOpenGL


class ImplicitCurve(VMobject, metaclass=ConvertToOpenGL):
    """An implicit curve (2D)

    Examples
    --------

    .. manim:: ExampleImplicitCurve
        :save_last_frame:

        class ExampleImplicitCurve(Scene):
            def func(self, x, y):
                return y ** 2 - x ** 3 + x

            def construct(self):
                curve = ImplicitCurve(self.func, (-2, 2), (-2, 2), color=RED)
                self.add(curve)
                self.wait()
    """

    def __init__(
        self,
        func: Callable[[np.ndarray], float],
        x_range: Tuple[float, float],
        y_range: Tuple[float, float],
        **kwargs
    ):
        self.func = func
        self.x_range = x_range
        self.y_range = y_range
        super().__init__(**kwargs)

    def generate_points(self):
        # Temporary for testing
        self.start_new_path(np.array([0, 0, 0]))
        self.add_points_as_corners(
            np.array(
                [
                    [self.x_range[0], self.y_range[0], 0],
                    [self.x_range[0], self.y_range[1], 0],
                    [self.x_range[1], self.y_range[1], 0],
                    [self.x_range[1], self.y_range[0], 0],
                ]
            )
        )
        return self
