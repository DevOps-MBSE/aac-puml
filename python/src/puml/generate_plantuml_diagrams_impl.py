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
COMPONENT_STRING = "component"
OBJECT_STRING = "object"
SEQUENCE_STRING = "sequence"
REQUIREMENTS_STRING = "requirements"


def before_puml_component_check(
    architecture_file: str, output_directory: str, run_check
) -> ExecutionResult:
    """
        Run the Check AaC command before the puml-component command.

        Args:
            architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
    generate a PlantUML component diagram.
            output_directory (str): The output directory into which the PlantUML (.puml) diagram file
    will be written.

       Returns:
            The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


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


def before_puml_sequence_check(
    architecture_file: str, output_directory: str, run_check
) -> ExecutionResult:
    """
        Run the Check AaC  command before the puml-sequence command.

        Args:
            architecture_file (str): A path to a YAML file containing an AaC-defined usecase from which
    to generate a PlantUML sequence diagram.

            output_directory (str): The output directory into which the PlantUML (.puml) diagram file
    will be written.



       Returns:
            The results of the execution of the  command.
    """

    # TODO: configure and call the check before command using puml-sequence command inputs
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The Check AaC check before handling for the puml-sequence command has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-sequence", status, messages)


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


def before_puml_object_check(
    architecture_file: str, output_directory: str, run_check
) -> ExecutionResult:
    """
        Run the Check AaC  command before the puml-object command.

        Args:
            architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
    generate a PlantUML object diagram.

            output_directory (str): The output directory into which the PlantUML (.puml) diagram file
    will be written.



       Returns:
            The results of the execution of the  command.
    """

    # TODO: configure and call the check before command using puml-object command inputs
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The Check AaC check before handling for the puml-object command has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-object", status, messages)


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


def before_puml_requirements_check(
    architecture_file: str, output_directory: str, run_check
) -> ExecutionResult:
    """
        Run the Check AaC  command before the puml-requirements command.

        Args:
            architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
    generate a PlantUML requirements diagram.

            output_directory (str): The output directory into which the PlantUML (.puml) diagram file
    will be written.



       Returns:
            The results of the execution of the  command.
    """

    # TODO: configure and call the check before command using puml-requirements command inputs
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []
    error_msg = ExecutionMessage(
        "The Check AaC check before handling for the puml-requirements command has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-requirements", status, messages)


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