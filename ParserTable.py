# Definición de keywords, non_terminal, terminal y grammar
keywords = [
    'doc', 'h1', 'h2', 'h3', 'p', 'b', 'i', 'url', 'img', 'table', 'r', 'hr', 'c', 'lb', 'list', 'item',
]

non_terminal = [
    'S', 'Doc', 'Section', 'SectionP', 'Element', 'Paragraph', 'ParagraphP', 'Content', 'Formated',
    'FormatedP', 'List', 'Items', 'ItemsP', 'Item', 'Table', 'Header' ,'Rows', 'RowsP', 'Columns', 'ColumnsP', 'Column',
]

terminal = [
    'doc', 'p', 'h1', 'h2', 'h3', 'text', 'h2', 'h3', 'url', 'img', 'lb', 'b', 'i', 'list', 'item', 'table', 'r', 'hr', 'c',
]

grammar = {
    "S": {
        "doc": ["Doc", "$"]
    },
    "Doc": {
        "doc": ["doc", "Section", "doc"]
    },
    "Section": {
        "p": ["Element", "SectionP"],
        "h1": ["Element", "SectionP"],
        "h2": ["Element", "SectionP"],
        "h3": ["Element", "SectionP"]
    },
    "SectionP": {
        "p": ["Element", "SectionP"],
        "h1": ["Element", "SectionP"],
        "h2": ["Element", "SectionP"],
        "h3": ["Element", "SectionP"],
        "doc": ["ε"]
    },
    "Element": {
        "p": ["p", "Paragraph", "p"],
        "h1": ["h1", "text", "h1"],
        "h2": ["h2", "text", "h2"],
        "h3": ["h3", "text", "h3"]
    },
    "Paragraph": {
        "text": ["Content", "ParagraphP"],
        "url": ["Content", "ParagraphP"],
        "img": ["Content", "ParagraphP"],
        "lb": ["Content", "ParagraphP"],
        "b": ["Content", "ParagraphP"],
        "i": ["Content", "ParagraphP"],
        "list": ["Content", "ParagraphP"],
        "table": ["Content", "ParagraphP"]
    },
    "ParagraphP": {
        "text": ["Content", "ParagraphP"],
        "url": ["Content", "ParagraphP"],
        "img": ["Content", "ParagraphP"],
        "lb": ["Content", "ParagraphP"],
        "b": ["Content", "ParagraphP"],
        "i": ["Content", "ParagraphP"],
        "list": ["Content", "ParagraphP"],
        "table": ["Content", "ParagraphP"],
        "p": ["ε"]
    },
    "Content": {
        "text": ["text"],
        "url": ["url", "text", "url"],
        "img": ["img", "text", "img"],
        "lb": ["lb"],
        "b": ["Formated"],
        "i": ["Formated"],
        "list": ["List"],
        "table": ["Table"]
    },
    "Formated": {
        "b": ["b", "FormatedP", "b"],
        "i": ["i", "FormatedP", "i"]
    },
    "FormatedP": {
        "text": ["text"],
        "b": ["Formated"],
        "i": ["Formated"]
    },
    "List": {
        "list": ["list", "Items", "list"]
    },
    "Items": {
        "item": ["item", "Item", "item", "ItemsP"]
    },
    "ItemsP": {
        "item": ["item", "Item", "item", "ItemsP"],
        "list": ["ε"]
    },
    "Item": {
        "text": ["text"],
        "b": ["Formated"],
        "i": ["Formated"]
    },
    "Table": {
        "table": ["table", "Header", "Rows", "table"]
    },
    "Header": {
        "hr": ["hr", "Columns", "hr"]
    },
    "Rows": {
        "r": ["r", "Columns", "r", "RowsP"]
    },
    "RowsP": {
        "r": ["r", "Columns", "r", "RowsP"],
        "table": ["ε"]
    },
    "Columns": {
        "c": ["c", "Column", "c", "ColumnsP"]
    },
    "ColumnsP": {
        "c": ["c", "Column", "c", "ColumnsP"],
        "r": ["ε"],
        "hr": ["ε"],
    },
    "Column": {
        "text": ["text"],
        "b": ["Formated"],
        "i": ["Formated"]
    }
}