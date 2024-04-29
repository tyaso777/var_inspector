# VarInspector

`VarInspector` is a Python package designed to inspect and display information about variables and objects in a Python environment. It provides an easy way to quickly understand the types, sizes, and other characteristics of variables within your code, making debugging and analysis much simpler.

## Features

- **Variable Overview**: Get detailed information about any variable, including its type, size, and value.
- **Advanced Inspection**: Offers detailed introspection for callables, modules, and other complex types.
- **Customizable Display**: Users can configure the maximum string length and the maximum number of rows to display, tailoring the output to their specific needs.

## Installation

Install `VarInspector` using pip:

    pip install var_inspector

Or, if you prefer to install from source:

    git clone https://github.com/tyaso777/var_inspector.git
    cd var_inspector
    pip install .

## Usage

Here's how to use `VarInspector`:

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

## Example Output
1. Display information about global variables by view_var():

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>User-defined and basic type global variables:</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>User-defined and basic type global variables:</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Size (MB)</th>
                    <th>Len</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Optional</td>
                    <td>_SpecialForm</td>
                    <td>0.00</td>
                    <td>-</td>
                    <td>typing.Optional</td>
                </tr>
                <tr>
                    <td>Sized</td>
                    <td>ABCMeta</td>
                    <td>0.00</td>
                    <td>-</td>
                    <td>&lt;class 'collections.abc.Sized'&gt;</td>
                </tr>
                <tr>
                    <td>VarInspector</td>
                    <td>type</td>
                    <td>0.00</td>
                    <td>-</td>
                    <td>&lt;class '__main__.VarInspector'&gt;</td>
                </tr>
                <tr>
                    <td>view_var</td>
                    <td>VarInspector</td>
                    <td>0.00</td>
                    <td>-</td>
                    <td>&lt;__main__.VarInspector object at 0x00000213C3AA0A10&gt;</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>

2. Inspect a specific variable by view_var(some_variable):
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Object Overview:</title>
        <style>
            table {
                width: 80%;
                margin: 20px auto;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }
            th {
                background-color: #f2f2f2;
            }
            td {
                vertical-align: top;
            }
        </style>
    </head>
    <body>
        <h1>Object Overview:</h1>
        <table>
            <tr>
                <th>Attribute</th>
                <th>Value</th>
            </tr>
            <tr>
                <td>Type</td>
                <td>list</td>
            </tr>
            <tr>
                <td>Module</td>
                <td>Unknown module</td>
            </tr>
            <tr>
                <td>Source File</td>
                <td>Source file not available</td>
            </tr>
            <tr>
                <td>File Path</td>
                <td>File not applicable</td>
            </tr>
            <tr>
                <td>Source Lines</td>
                <td>No source line info</td>
            </tr>
            <tr>
                <td>Size (MB)</td>
                <td>0.00</td>
            </tr>
            <tr>
                <td>Doc</td>
                <td>Built-in mutable sequence.<br><br>If no argument is given, the constructor creates a new empty list.<br>The argument must be an iterable if specified.</td>
            </tr>
        </table>
    </body>
    </html>


    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Attributes and methods of list:</title>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                table-layout: fixed;
            }
            th, td {
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
                word-wrap: break-word;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h1>Attributes and methods of list:</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Type</th>
                    <th>Signature</th>
                    <th>Size (MB)</th>
                    <th>Len</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>append</td>
                    <td>Method</td>
                    <td>(object, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Append object to the end of the list.</td>
                </tr>
                <tr>
                    <td>clear</td>
                    <td>Method</td>
                    <td>()</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Remove all items from list.</td>
                </tr>
                <tr>
                    <td>copy</td>
                    <td>Method</td>
                    <td>()</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Return a shallow copy of the list.</td>
                </tr>
                <tr>
                    <td>count</td>
                    <td>Method</td>
                    <td>(value, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Return number of occurrences of value.</td>
                </tr>
                <tr>
                    <td>extend</td>
                    <td>Method</td>
                    <td>(iterable, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Extend list by appending elements from the iterable.</td>
                </tr>
                <tr>
                    <td>index</td>
                    <td>Method</td>
                    <td>(value, start=0, stop=9223372036854775807, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Return first index of value. Raises ValueError if the value is not present.</td>
                </tr>
                <tr>
                    <td>insert</td>
                    <td>Method</td>
                    <td>(index, object, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Insert object before index.</td>
                </tr>
                <tr>
                    <td>pop</td>
                    <td>Method</td>
                    <td>(index=-1, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.</td>
                </tr>
                <tr>
                    <td>remove</td>
                    <td>Method</td>
                    <td>(value, /)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Remove first occurrence of value. Raises ValueError if the value is not present.</td>
                </tr>
                <tr>
                    <td>reverse</td>
                    <td>Method</td>
                    <td>()</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Reverse *IN PLACE*.</td>
                </tr>
                <tr>
                    <td>sort</td>
                    <td>Method</td>
                    <td>(*, key=None, reverse=False)</td>
                    <td>-</td>
                    <td>-</td>
                    <td>Sort the list in ascending order and return None. The sort is in-place and stable. If a key function is given, apply it once to each list item and sort them, ascending or descending, according to....</td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>

## Contributing

Contributions to `VarInspector` are welcome! However, please be aware that this project does not currently have any tests, and due to limited maintenance, there might be a delay in responding to contributions. While we appreciate your input, it may be more beneficial to consider creating a similar project of your own if you have significant changes or improvements in mind.

If you still wish to contribute, please feel free to fork the repository and submit your changes via a pull request. Here's a reminder that contributions might not be noticed promptly, but they are appreciated when spotted!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
