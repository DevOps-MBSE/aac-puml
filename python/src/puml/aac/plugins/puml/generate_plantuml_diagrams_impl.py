"""The AaC Generate PlantUML Diagrams plugin implementation module."""

# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
    MessageLevel,
)
from aac.in_out.files.aac_file import AaCFile
from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.context.source_location import SourceLocation
from typing import Any


plugin_name = "Generate PlantUML Diagrams"


def puml_component(architecture_file, output_directory) -> ExecutionResult:
    """Business logic for allowing puml-component command to perform Converts an AaC-defined system to a PlantUML component diagram.."""

    # TODO: implement plugin logic here
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The puml-component command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-component", status, messages)


def puml_sequence(architecture_file, output_directory) -> ExecutionResult:
    """Business logic for allowing puml-sequence command to perform Converts an AaC-defined usecase to PlantUML sequence diagram.."""

    # TODO: implement plugin logic here
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The puml-sequence command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-sequence", status, messages)


def puml_object(architecture_file, output_directory) -> ExecutionResult:
    """Business logic for allowing puml-object command to perform Convert an AaC-defined system to PlantUML object diagram.."""

    # TODO: implement plugin logic here
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The puml-object command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-object", status, messages)


def puml_requirements(architecture_file, output_directory) -> ExecutionResult:
    """Business logic for allowing puml-requirements command to perform Convert an AaC-defined system to a requirements diagram in PlantUML format.."""

    # TODO: implement plugin logic here
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The puml-requirements command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-requirements", status, messages)