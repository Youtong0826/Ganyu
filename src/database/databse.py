import json
import sqlite3
from typing import List, Any
from database.item import DatabaseItem

class Database():
    """
    Quick-Sqlite-Database
    """
    def __init__(self, path: str, name: str = "__default__", auto_init: Any = None) -> None:
        self.path = path
        self.conn = sqlite3.connect(path)
        self.name = name
        self.auto_init = auto_init

        c = self.conn.cursor()
        check = c.execute(
            f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.name}';")

        if (not list(check)):
            c = self.conn.cursor()
            c.execute(
                f'CREATE TABLE `{self.name}` (`key` CHAR(255) NOT NULL PRIMARY KEY, `value` JSON);')
            self.conn.commit()

    def __str__(self) -> str:
        return '{'+ ', '.join(map(str, self.get_all())) + '}'
    
    def __repr__(self) -> str:
        return f"<Database path={self.path} name={self.name} auto_init={self.auto_init}>"
    
    def set(self, key: Any, value: Any) -> Any:
        """
        Set value by key and return the value.
        """
        c = self.conn.cursor()
        c.execute(
            f'REPLACE INTO `{self.name}` VALUES ("{key}", \'{json.dumps(value)}\');')
        self.conn.commit()
        return value

    def get(self, key: Any, default: Any = None , no_init: bool = False) -> Any:
        """
        Get value by key.
        """
        c = self.conn.cursor()
        result = list(c.execute(f'SELECT `value` FROM `{self.name}` WHERE `key` == "{key}";'))

        if result:
            try:
                return json.loads(result[0][0])
            
            except:
                return result[0][0]
        
        elif default:
            return self.set(key, default)
            
        elif self.auto_init != None and not no_init: #有使用 auto init
            return self.set(key, self.auto_init)
        
        return None

    def get_all(self) -> List[DatabaseItem]:
        """
        Get all key and value as list
        """
        c = self.conn.cursor()
        return [DatabaseItem(item[0], item[1]) for item in list(c.execute(f'SELECT * FROM `{self.name}`;'))]

    def get_all_key(self) -> List[Any]:
        """
        Get all key as list
        """
        c = self.conn.cursor()
        return [item[0] for item in list(c.execute(f'SELECT `key` FROM `{self.name}`;'))]

    def delete(self, key: Any) -> None:
        """
        Delete item from database
        """
        c = self.conn.cursor()
        c.execute(f'DELETE FROM `{self.name}` WHERE `key` == "{key}";')
        self.conn.commit()

    def add(self, key: Any, value: Any) -> Any:
        """
        Add some value from the key and return the value.
        """
        return self.set(key, self.get(key) + value)

    
    def append(self, key: Any, item: Any) -> Any:
        """
        Append a item from the key and return the value. \n
        Note: The type of value must be List.
        """
        data: list = self.get(key)
        if (not isinstance(data, list)):
            raise TypeError("The type of value must be List.")
        
        data.append(item)
        return self.set(key, data)
        
    def substract(self, key: Any, value: Any) -> Any:
        """
        Substract some value from the key and return the value.
        """
        return self.set(key, self.get(key)-value)

    def remove(self, key: Any, item: Any) -> Any:
        """
        Remove a item from the key and return the value.
        Note: The type of value must be List. 
        """
        data: list = self.get(key)
        if (not isinstance(data, list)):
            raise TypeError("The type of value must be List.")
        
        data.remove(item)
        return self.set(key, data)

    def exists(self, key: Any) -> bool:
        """
        Check if key exists
        """
        return not (self.get(key, no_init=True) == None)

    def rename(self, name: Any) -> None:
        """
        Rename the table from database
        """
        c = self.conn.cursor()
        c.execute(f'ALTER TABLE `{self.name}` RENAME TO `{name}`;')
        self.conn.commit()

if __name__ == "__main__":
    pass
    # db = Database("test.db", auto_init=0)
    # print(repr(db))
    