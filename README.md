# miniargs

A wrapper of `argparse` which **I** can remember the APIs.

## Usage

### Basic

```python
import miniargs
p = miniargs.ArgumentParser()
p.add_int("--batch_size", default=128)
p.add_str("--optimizer", choices=["sgd", "adam"])
p.add_float("--lr", default=0.1)
p.add_true("--use_mixup")
p.add_multi_int("--step", default=[100, 150])
args = p.parse()
```

Parsed arguments are stored as an `Arguments` object.

```python
>>> print(args)
Arguments(batch_size=128, optimizer="sgd",...)
>>> args.batch_size
128
>>> args["batch_size"]
128
```

### Adavanced

```python
p.add_only_one_true("--distributed", "--multiprocess_distributed", must=True)
# Users chose only one of the arguments
...
if args.distributed:
    ...
if args.multiprocess_distributed:
    ...
```
