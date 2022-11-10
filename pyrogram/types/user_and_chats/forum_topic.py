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

import pyrogram
from pyrogram import raw
from pyrogram import types
from ..object import Object
from ... import utils


class ForumTopic(Object):
    """A Forum Topic.

    Parameters:
        message_thread_id (``int``):
            Unique identifier of the forum topic.

        title (``str``):
            Name of the topic.

        icon_color (``int``):
            Color of the topic icon in RGB format.

        icon_custom_emoji_id (``str``, *optional*):
            Unique identifier of the custom emoji shown as the topic icon.
    """

    def __init__(
        self,
        *,
        message_thread_id: int,
        title: str = None,
        icon_color: int = None,
        icon_custom_emoji_id: Optional[str] = None
    ):
        super().__init__(client)

        self.message_thread_id = message_thread_id
        self.title = title
        self.icon_color = icon_color
        self.icon_custom_emoji_id = icon_custom_emoji_id

    @staticmethod
    def _parse(client, forumtopic: "raw.types.ForumTopic") -> "ForumTopic":
        return ForumTopic(
            message_thread_id=forumtopic.message_thread_id,
            title=forumtopic.title,
            icon_color=forumtopic.icon_color,
            icon_custom_emoji_id=forumtopic.icon_custom_emoji_id,
            client=client
        )
