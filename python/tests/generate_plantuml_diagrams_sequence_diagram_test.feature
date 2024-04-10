# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.


Feature: Sequence Diagram Test

  Scenario: Output PlantUML sequence diagram for specified input file and output path.
  
      Given The {{puml.input.architecture-file}} contains a valid model.
      And The positional argument {{puml.input.output-directory}} contains a valid file path.
      When The aac app is run with the puml-sequence command.
      Then A PlantUML sequence diagram of the use case is written to the output directory.
      
    
  
  