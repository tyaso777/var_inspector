# %%
import inspect
import sys
import types
from collections.abc import Sized
from typing import Optional

import pandas as pd


class VarInspector:
    """
    A class to inspect and display information about variables and objects in a Python environment.

    Attributes:
        exclude_names (set[str]): Set of variable names to exclude from global display.
        descending (bool): Sort order for displaying global variables.
        max_str_length (int): Maximum length of string representation for values.
        max_rows (int): Maximum number of rows to display in the dataframe.

    Methods:
        __call__: Callable method to display information based on context.

    Examples:
        ```python
        # Creating an instance with custom settings
        from var_inspector import VarInspector
        view_var = VarInspector(max_str_length=300, max_rows=200)
        # or import view_var directly
        from var_inspector import view_var

        # Just invoking the view_var to display global variables with default settings
        view_var()

        # Displaying all global variables including special types
        view_var(include_advanced_details=True)

        # Displaying information about a specific variable
        some_variable = [1, 2, 3]
        view_var(some_variable)

        # Displaying information about a specific variable including special types
        view_var(some_variable, include_advanced_details=True)
        ```
    """

    def __init__(
        self,
        exclude_names: Optional[set[str]] = None,
        descending: bool = False,
        max_str_length: int = 300,
        max_rows: int = 300,
    ):
        if exclude_names is None:
            exclude_names = {"In", "Out", "_", "exit", "quit", "get_ipython"}
        self.exclude_names = exclude_names
        self.descending = (
            descending  # Boolean to determine if sorting in descending order
        )
        self.max_str_length = max_str_length
        self.max_rows = (
            max_rows if max_rows is not None else pd.get_option("display.max_rows")
        )

    def _format_value(self, value) -> str:
        return repr(value)

    def _get_size_mb(self, obj):
        """Estimate the size of a Python object in megabytes."""
        return sys.getsizeof(obj) / (1024**2)

    def _get_length(self, obj):
        """Get the length of an object if applicable."""
        if isinstance(obj, Sized):
            return len(obj)
        return "-"

    def __call__(self, var=None, include_advanced_details=False):
        """
        Callable method to display variable information based on the provided context.

        Args:
            var (Optional): Specific variable to inspect. If None, display global variables.
            include_advanced_details (bool): Whether to include all the cases (callables, modules, hidden attributes, special objects) in the display.
        """
        original_max_colwidth = pd.get_option("display.max_colwidth")
        original_max_rows = pd.get_option("display.max_rows")
        pd.set_option("display.max_colwidth", self.max_str_length)
        pd.set_option("display.max_rows", self.max_rows)
        try:
            if var is None:
                print("User-defined and basic type global variables:")
                self._display_globals(include_advanced_details=include_advanced_details)
            else:
                print("Object Overview:")
                self._display_overview(var)
                print(f"Attributes and methods of {type(var).__name__}:")
                self._display_attributes(
                    var, include_advanced_details=include_advanced_details
                )
        finally:
            pd.set_option("display.max_colwidth", original_max_colwidth)
            pd.set_option("display.max_rows", original_max_rows)

    def _display_overview(self, obj):
        """Display an overview of the object."""
        try:
            module = inspect.getmodule(obj)
            module_name = module.__name__ if module else "Unknown module"
            source_file = (
                inspect.getsourcefile(obj)
                if hasattr(obj, "__code__")
                else "Source file not available"
            )
        except TypeError:
            source_file = "Source file not applicable"

        try:
            file_path = inspect.getfile(obj)
        except TypeError:
            file_path = "File not applicable"

        try:
            source_lines = (
                inspect.getsourcelines(obj)
                if hasattr(obj, "__code__")
                else ("Not applicable", None)
            )
        except OSError:
            source_lines = ("Not applicable", None)

        overview_data = {
            "Type": [type(obj).__name__],
            "Module": [module_name],
            "Source File": [source_file],
            "File Path": [file_path],
            "Source Lines": [
                (
                    f"Starts at line {source_lines[1]}"
                    if source_lines[1]
                    else "No source line info"
                )
            ],
            "Size (MB)": [f"{self._get_size_mb(obj):.2f}"],
            "Doc": [inspect.getdoc(obj) or "No documentation available"],
        }
        df_overview = pd.DataFrame(overview_data)
        df_overview = df_overview.T  # Transpose to display as vertical records
        df_overview.columns = ["Value"]  # Rename columns after transpose
        display(df_overview)

    def _display_globals(self, include_advanced_details=False):
        data = []
        global_vars = {
            name: value
            for name, value in globals().items()
            if (
                include_advanced_details
                or (
                    not any(name.startswith(exclude) for exclude in self.exclude_names)
                    and not isinstance(
                        value,
                        (
                            types.ModuleType,
                            types.FunctionType,
                            types.BuiltinFunctionType,
                        ),
                    )
                    and not name.endswith("_")
                )
            )
        }
        sorted_vars = sorted(
            global_vars.items(), key=lambda x: x[0].lower(), reverse=self.descending
        )
        for name, value in sorted_vars:
            data.append(
                {
                    "Name": name,
                    "Type": type(value).__name__,
                    "Size (MB)": f"{self._get_size_mb(value):.2f}",
                    "Len": self._get_length(value),
                    "Value": self._format_value(value),
                }
            )
        df = pd.DataFrame(data)
        display(df)

    def _display_attributes(self, obj, include_advanced_details=False):
        data = []
        for attr in dir(obj):
            if include_advanced_details or not attr.startswith("_"):
                try:
                    value = getattr(obj, attr)
                    if callable(value):
                        doc = inspect.getdoc(value) or "No documentation available"
                        try:
                            sig = str(inspect.signature(value))
                        except ValueError:
                            sig = "N/A"
                        data.append(
                            {
                                "Name": attr,
                                "Type": "Method",
                                "Signature": sig,
                                "Size (MB)": "-",
                                "Len": "-",
                                "Value": doc if doc else "No documentation available",
                            }
                        )
                    else:
                        data.append(
                            {
                                "Name": attr,
                                "Type": type(value).__name__,
                                "Signature": "-",
                                "Size (MB)": f"{self._get_size_mb(value):.2f}",
                                "Len": self._get_length(value),
                                "Value": self._format_value(value),
                            }
                        )
                except AttributeError:
                    print(f"Attribute {attr} is not accessible.")
        df = pd.DataFrame(data)
        display(df)


# %%
# default instance
view_var = VarInspector(max_str_length=300, max_rows=300)

# %%
# Example usage
# a = "\n"
# b = "\\n"
# c = " \\n"
# example_instance = {"key": "value", "another_key": "another_value"}
# x = 10
# y = "Hello, world!"
# z = "This is a very long string that should be truncated because it exceeds the maximum allowed length."
# long_string_with_newlines = (
#     "This is a string with newlines.\nHere is a new line.\nAnd another one."
# )
# long_list = range(100)  # Now an iterable that will be displayed properly
# longlong_list = [[l for l in range(k)] for k in range(1, 100)]
# longlong_text_list = [z for k in range(1, 100)]

# import requests

# url = "https://pypi.org/project/truststore/"
# response = requests.get(url)

# view_var = VarInspector()

# view_var()

# view_var(include_advanced_details=True)

# view_var(view_var)

# view_var(response, include_advanced_details=True)

# %%
# Creating an instance with custom settings
from var_inspector import VarInspector
view_var = VarInspector(max_str_length=300, max_rows=200)
# or import view_var directly
from var_inspector import view_var

# %%
# Just invoking the view_var to display global variables with default settings
view_var()

# %%
# Displaying all global variables including special types
view_var(include_advanced_details=True)

# %%
# Displaying information about a specific variable
some_variable = [1, 2, 3]
view_var(some_variable)

# %%
# Displaying information about a specific variable including special types
view_var(some_variable, include_advanced_details=True)