from typing import Callable


class AppContext:

    class StateVariable:

        def __init__(
            self,
            initial_value: any = None,
            callbacks: Callable[[any], None] | list[Callable[[any], None]] = [],
        ):
            self._value = initial_value
            self._callbacks = callbacks if isinstance(callbacks, list) else [callbacks]

        def set_value(self, value: any):
            self._value = value
            for callback in self._callbacks:
                callback(self._value)

        def get_value(self) -> any:
            return self._value

        def add_callback(self, callback: Callable[[any], None]):
            self._callbacks.append(callback)

    _variables: dict[str, StateVariable] = {}

    @staticmethod
    def var(
        name: str,
        initial_value: any = object(),
        callbacks: Callable[[any], None] | list[Callable[[any], None]] = [],
    ) -> StateVariable:
        if name in AppContext._variables:
            return AppContext._variables[name]
        new_var = AppContext.StateVariable(initial_value, callbacks)
        AppContext._variables[name] = new_var
        return new_var

    @staticmethod
    def get_var_keys() -> list[str]:
        return AppContext._variables.keys()
