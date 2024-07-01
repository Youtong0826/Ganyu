import os

from typing import (
    Any,
    Union,
)

from discord import (
    Bot, 
    ActionRow,
    SelectMenu,
    Interaction, 
    ComponentType,
    Button as DiscordButton,
)

from discord.ui import (
    View,
    Button,
    Select
)

from lib.functions import get_now_time
from database import Database

class Bot(Bot):
    def __init__(self, description=None, database_path: str = None, *args, **options):
        super().__init__(description, *args, **options)
        self.__database_path = database_path
        
    @property
    def database(self):
        return Database(self.__database_path)
        
    def get_interaction_value(self, interaction: Interaction):
        return [data.get("components",{})[0].get("value") for data in interaction.data.get("components",{})]
    
    def get_select_value(self, interaction: Interaction, index: int = -1) -> Union[Any, list[Any]]:
        return interaction.data.get("values")[index] if index != -1 else interaction.data.get("values")
    
    def from_component(self, view: View, component: Union[ActionRow, DiscordButton, SelectMenu]):
        kwargs = component.to_dict()
        kwargs.pop('type')
        
        match component.type:
            case ComponentType.button:
                view.add_item(Button(**kwargs))
                
            case ComponentType.select:
                view.add_item(Select(**kwargs))
                
            case ComponentType.role_select:
                view.add_item(Select(select_type=ComponentType.role_select, **kwargs))
                
            case ComponentType.user_select:
                view.add_item(Select(select_type=ComponentType.user_select, **kwargs))
                
            case ComponentType.channel_select:
                view.add_item(Select(select_type=ComponentType.channel_select, **kwargs))
                
            case _:
                for c in component.children:
                    self.from_component(view, c)
                    
    def load_extension(self, folder: str, mode: str = "load", is_notice: bool = True) -> None:

        loading_method = {
            "load": super().load_extension,
            "reload": super().reload_extension,
            "unload": super().unload_extension
        }

        if is_notice:
            print(f"start {mode}ing {folder}")

        for Filename in os.listdir(f'src/{folder}'):
            if Filename.endswith(".py"):
                loading_method[mode](f"{folder}.{Filename[:-3]}")
                if is_notice:
                    print(f'-- {mode}ed "{Filename}"')

        print(f"{mode}ing {folder} end")
        
    def log(self, *text: str, sep: str = None):
        print(get_now_time().strftime('[%Y/%m/%d %H:%M:%S]'), *text, sep=sep)