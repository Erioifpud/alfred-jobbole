class Item:
    def __init__(self, title, sub_title='', valid=True, arg=None, uid=None, icon=None, auto_complete=None, icon_type=None):
        self.title = title
        self.sub_title = sub_title
        self.valid = valid
        self.arg = arg
        self.uid = uid
        self.icon = icon
        self.auto_complete = auto_complete
        self.icon_type = icon_type

    def get_dict(self):
        dict = {'title': self.title, 'subtitle': self.sub_title, 'valid': self.valid}
        if self.arg:
            dict['arg'] = self.arg
        if self.uid:
            dict['uid'] = self.uid
        if self.icon:
            icon = {'path': self.icon}
            if self.icon_type:
                icon['type'] = self.icon_type
            dict['icon'] = icon
        if self.auto_complete:
            dict['autocomplete'] = self.auto_complete
        return dict
