#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import raw
from ..object import Object


class ForumTopicEdit(Object):
    """A service message about a new forum topic edited in the chat.


    Parameters:
        title (``String``, *optional*):
            Name of the topic.

        icon_color (``Integer``, *optional*):
            Color of the topic icon in RGB format

        closed (``bool``, *optional*):
            Is the topic closed
    """

    def __init__(
        self, *,
        title: str = None,
        icon_color: int = None,
        closed: bool = None
    ):
        super().__init__()

        self.title = title
        self.icon_color = icon_color
        self.closed = closed

    @staticmethod
    def _parse(action: "raw.types.channelAdminLogEventActionEditTopic") -> "ForumTopicEdit":
        title: Optional[str] = None
        icon_color: Optional[int] = None
        closed: Optional[bool] = None

        return ForumTopicEdit(
            title=title,
            icon_color=icon_color,
            closed=closed
        )
