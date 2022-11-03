import argparse
from pydantic import BaseModel, Field
from redbird.repos import SQLRepo

class Item(BaseModel):
    id: int
    name: str = Field(description="Name of the item!", default='N.A.')

repo = SQLRepo(
    conn_string="sqlite:///example.db",
    table='items',
    model=Item,
    id_field='id',
    if_missing="create")

def create_item(**kwargs):
    repo.add(Item(**kwargs))

def read_item(item_id = None):
    if item_id is None:
        for item in repo:
            print(repr(item))
    else:
        print(repr(repo[item_id]))

def update_item(item_id, **values):
    values = {key:value for key,value in values.items() if value is not None}
    repo[item_id] = values
    repo.filter_by(id=2).update(**values)

def delete_item(item_id):
    del repo[item_id]

def add_model_to_parser(parser: argparse.ArgumentParser, model):
    fields = model.__fields__
    for name, field in fields.items():
        parser.add_argument(
            f"--{name}", 
            dest=name, 
            type=field.type_, 
            default=field.default,
            help=field.field_info.description,
        )

def parse_args(args=None):
    parser = argparse.ArgumentParser(prog='Simple CRUD app')
    subparsers = parser.add_subparsers(dest='action')
    parser_create = subparsers.add_parser("create", help="Create an item")
    parser_read = subparsers.add_parser("read", help="Read an item")
    parser_update = subparsers.add_parser("update", help="Update an item")
    parser_delete = subparsers.add_parser("delete", help="Delete an item")
    parser_read_all = subparsers.add_parser("read_all", help="Read items")
    parser_read.add_argument("item_id", nargs="?", help="ID of the item")
    for sub_parser in (parser_update, parser_delete):
        sub_parser.add_argument("item_id", help="ID of the item")
    add_model_to_parser(parser_create, model=Item)
    add_model_to_parser(parser_update, model=Item)
    return parser.parse_args(args)

def main(args=None):
    args = parse_args(args)
    args=vars(args)
    action = args.pop("action")
    func = {
        'create':create_item,
        'read':read_item,
        'update':update_item,
        'delete':delete_item
    }[action]
    return func(**args)

if __name__=='__main__':
    main()