'''
MIT License

Copyright (c) 2020 - Present nxtlo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from ..utils import assets
from datetime import datetime
from typing import (
    List,
    Sequence,
    Dict,
    Any,
    Optional,
    Union
)

class Clans(object):
    """
    A class that returns information about a Destiny2 Clan.
    """
    __slots__: Sequence[str] = ("response",)

    def __init__(self, data: Optional[Dict[str, Any]]) -> None:
        self.response: Dict[str, Any] = data.get("Response")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def __getitem__(self, item) -> None:
        for _item in self.response.values():
            return _item[item]

    @property
    def get(self) -> None:
        return self.__getitem__

    @property
    def id(self) -> Optional[int]:
        """
        Returns
        --------
        :class:`int`
            The clan's id.
        """
        return self.get('groupId')

    @property
    def name(self) -> Optional[Any]:
        """
        Returns
        --------
        :class:`str`
            The clan's name.
        """
        return self.get('name')

    @property
    def created_at(self) -> Optional[datetime]:
        """
        Returns
        --------
        :class:`datetime.datetime`:
            When was the clan created at.
        """
        return self.get('creationDate')

    @property
    def edited_at(self) -> Optional[datetime]:
        """
        Returns
        --------
        :class:`datetime.datetime`:
            last time the clan was updated.
        """
        return self.get("modificationDate")

    @property
    def member_count(self) -> int:
        """
        Returns
        --------
        :class:`int`
            The clan's member count.
        """
        return self.get("memberCount")

    @property
    def description(self) -> Optional[Any]:
        """
        Returns
        --------
        :class"`str`:
            The clan's long description.
        """
        return self.get("about")

    @property
    def is_public(self) -> bool:
        """
        Returns
        --------
        :class:`bool`
            Returns `True` if the clan is Public, `False` if not.
        """
        return self.get("isPublic")

    @property
    def banner(self) -> Optional[str]:
        """
        Returns
        --------
        The clan's banner.
        """
        return assets.ImageProtocol(self.get("bannerPath"))

    @property
    def avatar(self) -> Optional[str]:
        """
        Returns
        --------
        :class:`str`
            The clan's avatar path.
        """
        return assets.ImageProtocol(self.get("avatarPath"))

    @property
    def about(self) -> Optional[Any]:
        """
        Returns
        --------
        :class:`str`
            The clans's short info.
        """
        return self.get("motto")

    @property
    def tag(self) -> Optional[Any]:
        """
        Returns
        --------
        :class:`str`
            The clans's tag.
        """
        return self.get("clanInfo")['clanCallsign']


    @property
    def owner(self) -> Any:
        """
        Returns
        --------
        :class:`str`
            The clan owner's name.
        """
        for item in self.response['founder']['destinyUserInfo'].values():
            return item

class ClanAdmins:
    ...