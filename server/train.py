class Train:
    def __init__(self, klass):
        self.klass = klass
        self.methods = klass.register()
