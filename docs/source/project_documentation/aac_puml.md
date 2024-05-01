# AaC PUML

The AaC PUML plugin evaluates an AaC model for various pertinent structures in order to produce PUML component, object, sequence, or requirements diagrams. For more information on these model types, view [Support PUML Diagrams](supported_puml_diagrams)

It will run `check` against the provided model file first to confirm it is valid and useable. This step will return any errors that are found.

If the provided model does not contain the pertinent structures for generating the requested PUML diagram type, an error notice will be given.

If the provided model contains the pertinent structures for the requested PUML diagram type, then an output confirmation message will be given.

## puml-component Command

```bash
aac puml-component my_model.aac output/directory
```

## Arguments

### Classification

The `--classification` argument will allow a user to provide a classification level for adding header and footer markings to the output diagram file.

## Help

```bash
$ aac puml-component
Usage: aac puml-component [OPTIONS] ARCHITECTURE_FILE OUTPUT_DIRECTORY

Options:
  --classification TEXT  The level of classification for the output diagram
                         file.
  -h, --help             Show this message and exit.
```

## Examples

For viewing example input and output of executing this command, view [Component Examples](component_examples).

## puml-object Command

```bash
aac puml-object my_model.aac output/directory
```

## Arguments

### Classification

The `--classification` argument will allow a user to provide a classification level for adding header and footer markings to the output diagram file.

## Help

```bash
$ aac puml-object
Usage: aac puml-object [OPTIONS] ARCHITECTURE_FILE OUTPUT_DIRECTORY

Options:
  --classification TEXT  The level of classification for the output diagram
                         file.
  -h, --help             Show this message and exit.
```

## Examples

For viewing example input and output of executing this command, view [Object Examples](object_examples).

## puml-requirements Command

```bash
aac puml-requirements my_model.aac output/directory
```

## Arguments

### Classification

The `--classification` argument will allow a user to provide a classification level for adding header and footer markings to the output diagram file. 

## Help

```bash
$ aac puml-requirements
Usage: aac puml-requirements [OPTIONS] ARCHITECTURE_FILE OUTPUT_DIRECTORY

Options:
  --classification TEXT  The level of classification for the output diagram
                         file.
  -h, --help             Show this message and exit.
```

## Examples

For viewing example input and output of executing this command, view [Requirements Examples](requirements_examples)

## puml-sequence Command

```bash
aac puml-sequence my_model.aac output/directory
```

## Arguments

### Classification

The `--classification` argument will allow a user to provide a classification level for adding header and footer markings to the output diagram file.

## Help

```bash
$ aac puml-sequence
Usage: aac puml-sequence [OPTIONS] ARCHITECTURE_FILE OUTPUT_DIRECTORY

Options:
  --classification TEXT  The level of classification for the output diagram
                         file.
  -h, --help             Show this message and exit.
```

## Examples

For viewing example input and output of executing this command, view [Sequence Examples](sequence_examples).
