from typing import Optional, Union

from beartype import beartype

from flet.constrained_control import ConstrainedControl
from flet.control import OptionalNumber
from flet.ref import Ref
from flet.types import AnimationValue, OffsetValue, RotateValue, ScaleValue

try:
    from typing import Literal
except:
    from typing_extensions import Literal


LabelPosition = Literal[None, "right", "left"]


class Radio(ConstrainedControl):
    def __init__(
        self,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[bool, int] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        tooltip: str = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        label: str = None,
        label_position: LabelPosition = None,
        value: str = None,
        autofocus: bool = None,
        on_focus=None,
        on_blur=None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )
        self.value = value
        self.label = label
        self.label_position = label_position
        self.autofocus = autofocus
        self.on_focus = on_focus
        self.on_blur = on_blur

    def _get_control_name(self):
        return "radio"

    # value
    @property
    def value(self):
        return self._get_attr("value", def_value="")

    @value.setter
    def value(self, value):
        self._set_attr("value", value)

    # label
    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

    # label_position
    @property
    def label_position(self):
        return self._get_attr("labelPosition")

    @label_position.setter
    @beartype
    def label_position(self, value: LabelPosition):
        self._set_attr("labelPosition", value)

    # on_focus
    @property
    def on_focus(self):
        return self._get_event_handler("focus")

    @on_focus.setter
    def on_focus(self, handler):
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    def on_blur(self):
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler):
        self._add_event_handler("blur", handler)

    # autofocus
    @property
    def autofocus(self):
        return self._get_attr("autofocus", data_type="bool", def_value=False)

    @autofocus.setter
    @beartype
    def autofocus(self, value: Optional[bool]):
        self._set_attr("autofocus", value)
