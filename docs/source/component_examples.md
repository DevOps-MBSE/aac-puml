# Component Examples

## Basic Command Execution

```bash
$ aac puml-component ./tests/alarm_clock/alarm_clock.yaml ./tests/alarm_clock/diagrams/component
All AaC constraint checks were successful.
Wrote PUML Component Diagram(s) to ./tests/alarm_clock/diagrams/component/.
```

## Basic Command Output

```
@startuml AlarmClock Component Diagram
title AlarmClock Component Diagram

interface Timestamp

component "AlarmClock" {
  component "Clock"
  Clock --> Timestamp : currentTime

  interface TimerAlert
  component "ClockTimer"
  Timestamp --> ClockTimer : targetTime
  Timestamp --> ClockTimer : currentTime
  ClockTimer --> TimerAlert : timerAlert

  interface AlarmNoise
  component "ClockAlarm"
  TimerAlert --> ClockAlarm : timerAlert
  ClockAlarm --> AlarmNoise : alarmNoise

}
Timestamp --> AlarmClock : targetTime

@enduml
```

## Command with Classification Execution

```bash
$ aac puml-component ./tests/alarm_clock/alarm_clock.yaml ./tests/alarm_clock/diagrams/component --classification unclassified
All AaC constraint checks were successful.
Wrote PUML Component Diagram(s) to ./tests/alarm_clock/diagrams/component/.
```

## Command with Classification Output

```
##### UNCLASSIFIED #####

@startuml AlarmClock Component Diagram
title AlarmClock Component Diagram

interface Timestamp

component "AlarmClock" {
  component "Clock"
  Clock --> Timestamp : currentTime

  interface TimerAlert
  component "ClockTimer"
  Timestamp --> ClockTimer : targetTime
  Timestamp --> ClockTimer : currentTime
  ClockTimer --> TimerAlert : timerAlert

  interface AlarmNoise
  component "ClockAlarm"
  TimerAlert --> ClockAlarm : timerAlert
  ClockAlarm --> AlarmNoise : alarmNoise

}
Timestamp --> AlarmClock : targetTime

@enduml

##### UNCLASSIFIED #####
```

## Command Execution Failure

```bash

```
