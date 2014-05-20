#asymm-fields
=============

Provides some django model fields, most of which are thin wrappers, but with 
more semantic names

## Fields

### CommentField / COMMENT_LENGTH

Thin wrapper around `CharField` with `max_length` set to `COMMENT_LENGTH`

default length :: 1024 chars

### IntegerRangeField

Provides the `min` and `max` attributes to the html `<input>` for django before 1.6

### LongMessageField / LONG_MESSAGE_LENGTH

Thin wrapper around `CharField` with `max_length` set to `LONG_MESSAGE_LENGTH`

default length :: 255 chars

### LongNameField / LONG_NAME_LENGTH

Thin wrapper around `CharField` with `max_length` set to `LONG_NAME_LENGTH`.

Designed to hold a first and last name, length = (SHORT_NAME_LENGTH * 2)  + 5

default length :: 285 chars

### QtyField / DollarField

Thin wrapper around `DecimalField` with `default` set to `Decimal('0.00')`, `max_digits` 
set to 15, and `decimal_places` set to 2.

`DollarField` is an alias for `QtyField`

### ZERO_QTY / ZERO_DOLLAR

Both are alias for `Decimal('0.00')`

### ShortMessageField / SHORT_MESSAGE_LENGTH

Thin wrapper around `CharField` with `max_length` set to `SHORT_MESSAGE_LENGTH`

default length :: 140 chars; the length of a typical SMS

### ShortNameField / SHORT_NAME_LENGTH

Thin wrapper around `CharField` with `max_length` set to `SHORT_NAME_LENGTH`

default length :: 50 char; should be enough to hold either a first, or last, name.

### UUIDField

Uses the first 10 characters of a uuid4 value. Overrides `pre_save` in order to 
check for uniqueness.


## TODO

* Speed up `UUIDField` so that it doesn't use `pre_save`
* Django 1.7 migrations and tests
