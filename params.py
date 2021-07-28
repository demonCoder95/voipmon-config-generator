class ConfigParameter():

    # Each paramter has a name, value, default_value and description
    def __init__(self, p_name, p_value, p_def_value, p_desc):
        self.p_name = p_name
        self.p_value = p_value
        self.p_def_value = p_def_value
        self.p_desc = p_desc

    # Get methods for parameters
    def get_name(self):
        return self.p_name

    def get_value(self):
        return self.p_value

    def get_def_value(self):
        return self.p_def_value

    def get_desc(self):
        return self.p_desc

    # Set methods for parameters
    
    # No set method needed for parameter name, it is set only once in the
    # constructor and never changes

    def set_value(self, value):
        self.p_value = value

    # No set method needed for default value, it is set only once in the
    # constructor and never changes

    # No set method needed for description, it is set only once in the
    # constructor and never changes