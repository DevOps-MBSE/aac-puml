# Object Examples

## Basic Command Execution

```bash
$ aac puml-object ./tests/alarm_clock/alarm_clock.yaml ./tests/alarm_clock/diagrams/object
All AaC constraint checks were successful.
Wrote PUML Object Diagram(s) to ./tests/alarm_clock/diagrams/object/.
```

## Basic Command File Content

```
@startuml AlarmClock Object Diagram
title AlarmClock Object Diagram

object AlarmClock

AlarmClock *-- ClockAlarm
AlarmClock *-- ClockTimer
AlarmClock *-- Clock

@enduml
```

## Command with Classification Execution

```bash
$ aac puml-object ./tests/alarm_clock/alarm_clock.yaml ./tests/alarm_clock/diagrams/object --classification unclassified
All AaC constraint checks were successful.
Wrote PUML Object Diagram(s) to ./tests/alarm_clock/diagrams/object/.
```

## Command with Classification File Content

```
##### UNCLASSIFIED #####

@startuml AlarmClock Object Diagram
title AlarmClock Object Diagram

object AlarmClock

AlarmClock *-- ClockAlarm
AlarmClock *-- ClockTimer
AlarmClock *-- Clock

@enduml

##### UNCLASSIFIED #####
```

## Command Execution Failure

```bash
$ aac puml-object ./tests/alarm_clock/structures.yaml ./tests/alarm_clock/diagrams/object
No applicable model definitions to generate an object diagram.
```

## Generated Files

Include screen shot of file tree, need to do from different comp.
