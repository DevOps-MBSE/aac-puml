# Requirements Examples

## Basic Command Execution

```bash
$ aac puml-requirements ./tests/calc/spec/Add_SRS.yaml ./tests/calc/diagrams/requirements --classification unclassified
All AaC constraint checks were successful.
Wrote PUML Requirements Diagram(s) to ./tests/calc/diagrams/requirements.
```

## Basic Command File Content

```
@startuml Add Requirements Diagram

mainframe **req** [Package] **Add** [Requirements]

object "<<Test>> **Add**" as Add {
    id = ADD-1
    Text = When receiving an add message, the calculator shall respond with the sum of the provided values.
    TADI = Test
    }

SM-1 +-- ADD-1
@enduml
```



## Command with Classification Execution

```bash
$ aac puml-requirements ./tests/calc/spec/Add_SRS.yaml ./tests/calc/diagrams/requirements --classification unclassified
All AaC constraint checks were successful.
Wrote PUML Requirements Diagram(s) to ./tests/calc/diagrams/requirements.
```

## Command with Classification File Content

```
##### UNCLASSIFIED #####

@startuml Add Requirements Diagram

mainframe **req** [Package] **Add** [Requirements]

object "<<Test>> **Add**" as Add {
    id = ADD-1
    Text = When receiving an add message, the calculator shall respond with the sum of the provided values.
    TADI = Test
    }

SM-1 +-- ADD-1
@enduml

##### UNCLASSIFIED #####
```

## Command Execution Failure

```bash
$ aac puml-requirements ./tests/alarm_clock/structures.yaml ./tests/alarm_clock/diagrams/requirements
No applicable requirement specification definitions to generate a requirements diagram.
```

## Generated Files

Include screen shot of file tree, need to do from different comp.
