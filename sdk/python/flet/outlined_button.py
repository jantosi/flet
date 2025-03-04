from typing import Optional, Union

from beartype import beartype

from flet.buttons import ButtonStyle
from flet.constrained_control import ConstrainedControl
from flet.control import Control, OptionalNumber
from flet.ref import Ref
from flet.types import AnimationValue, OffsetValue, RotateValue, ScaleValue


class OutlinedButton(ConstrainedControl):
    def __init__(
        self,
        text: str = None,
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
        icon: str = None,
        icon_color: str = None,
        style: ButtonStyle = None,
        content: Control = None,
        autofocus: bool = None,
        on_click=None,
        on_long_press=None,
        on_hover=None,
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

        self.text = text
        self.icon = icon
        self.icon_color = icon_color
        self.style = style
        self.content = content
        self.autofocus = autofocus
        self.on_click = on_click
        self.on_long_press = on_long_press
        self.on_hover = on_hover

    def _get_control_name(self):
        return "outlinedbutton"

    def _before_build_command(self):
        super()._before_build_command()
        self._set_attr_json("style", self.__style)

    def _get_children(self):
        if self.__content == None:
            return []
        self.__content._set_attr_internal("n", "content")
        return [self.__content]

    # text
    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)

    # icon
    @property
    def icon(self):
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value):
        self._set_attr("icon", value)

    # icon_color
    @property
    def icon_color(self):
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value):
        self._set_attr("iconColor", value)

    # style
    @property
    def style(self):
        return self.__style

    @style.setter
    @beartype
    def style(self, value: Optional[ButtonStyle]):
        self.__style = value

    # on_click
    @property
    def on_click(self):
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler):
        self._add_event_handler("click", handler)

    # on_long_press
    @property
    def on_long_press(self):
        return self._get_event_handler("long_press")

    @on_long_press.setter
    def on_long_press(self, handler):
        self._add_event_handler("long_press", handler)

    # content
    @property
    def content(self):
        return self.__content

    @content.setter
    @beartype
    def content(self, value: Optional[Control]):
        self.__content = value

    # autofocus
    @property
    def autofocus(self):
        return self._get_attr("autofocus", data_type="bool", def_value=False)

    @autofocus.setter
    @beartype
    def autofocus(self, value: Optional[bool]):
        self._set_attr("autofocus", value)

    # on_hover
    @property
    def on_hover(self):
        return self._get_event_handler("hover")

    @on_hover.setter
    def on_hover(self, handler):
        self._add_event_handler("hover", handler)
        if handler != None:
            self._set_attr("onHover", True)
        else:
            self._set_attr("onHover", None)
