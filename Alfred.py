from Item import Item
import json
import sys

class Alfred:
    def __init__(self):
        self.items = []
        self.args = sys.argv[1:]

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.remove(item)

    def clear(self):
        self.items = []

    def remove_item_by_uid(self, uid):
        pass

    def get_arg(self, id):
        return self.args[id]

    def get_arg_len(self):
        return len(self.args)

    def show(self):
        items = map(lambda x: x.get_dict(), self.items)
        dict = {'items': list(items)}
        print(json.dumps(dict))