import ttk

framestyle = ttk.Style()
framestyle.theme_create('framestyle', parent="default",
                        settings = {"Input.TFrame":
                                        {"configure":
                                             {'selectbackground': 'blue',
                                              'fieldbackground': 'white',
                                              'background': 'white'}}})
framestyle.theme_use("framestyle")