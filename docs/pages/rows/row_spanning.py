from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Rows - Row Spanning",
)

text1 = """
# Row Spanning
By default, each cell will take up the height of one row. You can change this behaviour to allow cells to span multiple rows. This feature is similar to 'cell merging' in Excel or 'row spanning' in HTML tables.

### Configuring Row Spanning
To allow row spanning, the grid must have property suppressRowTransform=true. Row spanning is then configured at the column definition level. To have a cell span more than one row, return how many rows to span in the callback colDef.rowSpan.

- rowSpan (Function) By default, each cell will take up the height of one row. You can change this behaviour to allow cells to span multiple rows.

```

columnDefs =  [
    {
        'field': 'country',
        # row span is 2 for rows with Russia, but 1 for everything else
        'rowSpan': {'function': "params.data.country === 'Russia' ? 2 : 1"}
    },
    # other column definitions ...
]
 
grid = dag.AgGrid( 
    columnDefs=columnDefs,
    dashGridOptions = {'suppressRowTransform': True}
    # other grid options
)
```    

> Setting the property `suppressRowTransform` to True stops the grid positioning rows using CSS transform and instead the grid will use CSS top. For an explanation of the difference between these two methods see the article JavaScript GPU Animation with Transform and Translate. The reason row span will not work with CSS transform is that CSS transform creates a stacking context which constrains CSS z-index from placing cells on top of other cells in another row. Having cells extend into other rows is necessary for row span which means it will not work when using CSS transform. The downside to not using transform is performance; row animation (after sort or filter) will be slower.

### Row Spanning Simple Example
Below is a simple example using row spanning. The example doesn't make much sense, it just arbitrarily sets row span on some cells for demonstration purposes.

- The Athlete column is configured to span 2 rows for 'Aleksey Nemov' and 4 rows for 'Ryan Lochte'.
- The Athlete column is configured to apply a CSS class to give a background to the cell. This is important because if a background was not set, the cell background would be transparent and the underlying cell would still be visible.
"""


text3 = """
### Constraints with Row Spanning
Row Spanning breaks out of the row / cell calculations that a lot of features in the grid are based on. If using Row Spanning, be aware of the following:

- Responsibility is with the developer to not span past the last row. This is especially true if sorting and filtering (e.g. a cell may span outside the grid after the data is sorted and the cell's row ends up at the bottom of the grid).
- Responsibility is with the developer to apply a background style to spanning cells so that overwritten cells cannot be seen.
- Overwritten cells will still exist, but will not be visible. This means cell navigation will go to the other cells - e.g. if a row spanned cell has focus, and the user hits the 'arrow down' key, the focus will go to a hidden cell.
- Row span does not work with dynamic row height or auto-height. The row span assumes default row height is used when calculating how high the cell should be.
- Sorting and filtering will provide strange results when row spanning. For example a cell may span 4 rows, however applying a filter or a sort will probably change the requirements of what rows should be spanned.
- Range Selection will not work correctly when spanning cells. This is because it is not possible to cover all scenarios, as a range is no longer a perfect rectangle.

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rows.row_spanning", make_layout=make_tabs),
        make_md(text3)
        # up_next("text"),
    ],
)
