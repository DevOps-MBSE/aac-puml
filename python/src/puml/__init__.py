"""__init__.py module for the Generate PlantUML Diagrams plugin."""

# WARNING - DO NOT EDIT - YOUR CHANGES WILL NOT BE PROTECTED.
# This file is auto-generated by the aac gen-plugin and may be overwritten.

from os.path import join, dirname

from aac.execute import hookimpl
from aac.execute.plugin_runner import PluginRunner
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
)
from aac.context.language_context import LanguageContext
from aac.plugins.check import run_check
from aac.plugins.generate import run_generate


from puml.generate_plantuml_diagrams_impl import (
    plugin_name,
    puml_component,
    before_puml_component_check,
    after_puml_component_generate,
    puml_sequence,
    before_puml_sequence_check,
    after_puml_sequence_generate,
    puml_object,
    before_puml_object_check,
    after_puml_object_generate,
    puml_requirements,
    before_puml_requirements_check,
    after_puml_requirements_generate,
)

generate_plantuml_diagrams_aac_file_name = "generate_plantuml_diagrams.aac"


def run_puml_component(
    architecture_file: str, output_directory: str
) -> ExecutionResult:
    """
    Converts an AaC-defined system to a PlantUML component diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the plugin puml-component command.
    """
    result = ExecutionResult(plugin_name, "puml-component", ExecutionStatus.SUCCESS, [])

    puml_component_check_result = before_puml_component_check(
        architecture_file, output_directory, run_check
    )
    if not puml_component_check_result.is_success():
        return puml_component_check_result
    else:
        result.add_messages(puml_component_check_result.messages)

    component_content, puml_component_result = puml_component(architecture_file, output_directory)
    if not puml_component_result.is_success():
        return puml_component_result
    else:
        result.add_messages(puml_component_result.messages)

    puml_component_generate_result = after_puml_component_generate(
        architecture_file, output_directory, run_generate
    )
    if not puml_component_generate_result.is_success():
        return puml_component_generate_result
    else:
        result.add_messages(puml_component_generate_result.messages)

    return result


def run_puml_sequence(architecture_file: str, output_directory: str) -> ExecutionResult:
    """
    Converts an AaC-defined use case to PlantUML sequence diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the plugin puml-sequence command.
    """
    result = ExecutionResult(plugin_name, "puml-sequence", ExecutionStatus.SUCCESS, [])

    puml_sequence_check_result = before_puml_sequence_check(
        architecture_file, output_directory, run_check
    )
    if not puml_sequence_check_result.is_success():
        return puml_sequence_check_result
    else:
        result.add_messages(puml_sequence_check_result.messages)

    sequence_content, puml_sequence_result = puml_sequence(architecture_file, output_directory)
    if not puml_sequence_result.is_success():
        return puml_sequence_result
    else:
        result.add_messages(puml_sequence_result.messages)

    puml_sequence_generate_result = after_puml_sequence_generate(
        architecture_file, output_directory, run_generate
    )
    if not puml_sequence_generate_result.is_success():
        return puml_sequence_generate_result
    else:
        result.add_messages(puml_sequence_generate_result.messages)

    return result


def run_puml_object(architecture_file: str, output_directory: str) -> ExecutionResult:
    """
    Convert an AaC-defined system to PlantUML object diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the plugin puml-object command.
    """
    result = ExecutionResult(plugin_name, "puml-object", ExecutionStatus.SUCCESS, [])

    puml_object_check_result = before_puml_object_check(
        architecture_file, output_directory, run_check
    )
    if not puml_object_check_result.is_success():
        return puml_object_check_result
    else:
        result.add_messages(puml_object_check_result.messages)

    puml_object_result = puml_object(architecture_file, output_directory)
    if not puml_object_result.is_success():
        return puml_object_result
    else:
        result.add_messages(puml_object_result.messages)

    puml_object_generate_result = after_puml_object_generate(
        architecture_file, output_directory, run_generate
    )
    if not puml_object_generate_result.is_success():
        return puml_object_generate_result
    else:
        result.add_messages(puml_object_generate_result.messages)

    return result


def run_puml_requirements(
    architecture_file: str, output_directory: str
) -> ExecutionResult:
    """
    Convert an AaC-defined system to a requirements diagram in PlantUML format.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the plugin puml-requirements command.
    """
    result = ExecutionResult(
        plugin_name, "puml-requirements", ExecutionStatus.SUCCESS, []
    )

    puml_requirements_check_result = before_puml_requirements_check(
        architecture_file, output_directory, run_check
    )
    if not puml_requirements_check_result.is_success():
        return puml_requirements_check_result
    else:
        result.add_messages(puml_requirements_check_result.messages)

    puml_requirements_result = puml_requirements(architecture_file, output_directory)
    if not puml_requirements_result.is_success():
        return puml_requirements_result
    else:
        result.add_messages(puml_requirements_result.messages)

    puml_requirements_generate_result = after_puml_requirements_generate(
        architecture_file, output_directory, run_generate
    )
    if not puml_requirements_generate_result.is_success():
        return puml_requirements_generate_result
    else:
        result.add_messages(puml_requirements_generate_result.messages)

    return result


@hookimpl
def register_plugin() -> None:
    """
    Registers information about the plugin for use in the CLI.
    """

    active_context = LanguageContext()
    generate_plantuml_diagrams_aac_file = join(
        dirname(__file__), generate_plantuml_diagrams_aac_file_name
    )
    definitions = active_context.parse_and_load(generate_plantuml_diagrams_aac_file)

    generate_plantuml_diagrams_plugin_definition = [
        definition for definition in definitions if definition.name == plugin_name
    ][0]

    plugin_instance = generate_plantuml_diagrams_plugin_definition.instance
    for file_to_load in plugin_instance.definition_sources:
        active_context.parse_and_load(file_to_load)

    plugin_runner = PluginRunner(
        plugin_definition=generate_plantuml_diagrams_plugin_definition
    )
    plugin_runner.add_command_callback("puml-component", run_puml_component)
    plugin_runner.add_command_callback("puml-sequence", run_puml_sequence)
    plugin_runner.add_command_callback("puml-object", run_puml_object)
    plugin_runner.add_command_callback("puml-requirements", run_puml_requirements)

    active_context.register_plugin_runner(plugin_runner)
