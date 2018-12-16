# miniargs

A wrapper of `argparse` which **I** can remember the APIs.

## usage

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

```python
>>> print(args)
Arguments(batch_size=128, optimizer="sgd",...)
>>> args.batch_size
128
>>> args["batch_size"]
128
```
