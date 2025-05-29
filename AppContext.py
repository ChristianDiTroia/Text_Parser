class AppContext:

    class _StateVariable:

        def __init__(
            self,
            name: str,
            initial_value: any = None,
            callbacks: callable[[], None] | list[callable[[], None]] = [],
        ):
            self._value = initial_value
            self._callbacks = callbacks if isinstance(callbacks, list) else [callbacks]
            AppContext._variables[name] = self

        def set_value(self, value: any):
            self._value = value
            for callback in self._callbacks:
                callback()

        def get_value(self) -> any:
            return self._value

        def add_callback(self, callback: callable[[], None]):
            self._callbacks.append(callback)

    _variables: dict[str, _StateVariable] = {}

    @staticmethod
    def assign_var(
        name: str,
        initial_value: any = None,
        callback: callable[[], None] = lambda: None,
    ):
        return AppContext._StateVariable(name, initial_value, callback)

    @staticmethod
    def get_var(var_name):
        return AppContext._variables.get(var_name, None)

    @staticmethod
    def get_var_keys():
        return AppContext._variables.keys()


# TODO:
# Make custom app context that manages state variables
#   - make each variable except a callback function that is executed when variable state changes
#   - each variable should be accessed indirectly so that we can track state change
#   - App context will have a static method to get each variable based on name such as get_var()
#   - everytime an instance is made with the constructor, it will register the variable in a dict
