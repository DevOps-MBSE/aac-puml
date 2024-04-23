"""The AaC Generate PlantUML Diagrams plugin implementation module."""
# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
import yaml

from os import path
from typing import Callable, Optional

from aac.context.definition import Definition
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
    MessageLevel,
)
from aac.in_out.parser._parse_source import parse

from .helpers.component_helpers import model_sort
from .helpers.sequence_helpers import sort_use_case_components
from .helpers.object_helpers import get_object_data
from .helpers.requirements_helpers import get_requirements_defs

plugin_name = "Generate PlantUML Diagrams"


def before_puml_component_check(architecture_file: str, run_check: Callable) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-component command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_component(architecture_file: str, output_directory: str, classification: Optional[str]) -> tuple[str, ExecutionResult]:
    """
    Business logic for allowing puml-component command to perform the conversion of an AaC-defined system to a PlantUML component diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (Optional[str]): The level of classification for the output diagram file, or none if not provided.

    Returns:
        The YAML string to use in generating the output component diagram(s).
        ExecutionResult of the puml-component command for the PUML plugin.
    """
    # Initialize ExecutionResult for the puml-component command
    status = ExecutionStatus.GENERAL_FAILURE
    messages = []

    # Parse the input file to extract the definitions to sort
    parsed_file = parse(architecture_file)

    # Sort definitions into required data
    classification = classification.upper()
    component_data = model_sort(models=parsed_file, defined_interfaces=set(), classification=classification)

    # Create a List of strings containing the sorted data definitions
    yaml_list = []
    for model in component_data:
        yaml_list.append([{"model": model}])

    # Concatenate data definitions into a single string in yaml format
    new_file = ""
    for yaml_object in yaml_list:
        new_file = new_file + yaml.safe_dump_all(yaml_object, default_flow_style=False, sort_keys=False, explicit_start=True)

    # Check for if the passed data actually contained model definitions and update ExecutionResult
    if len(component_data) < 1:
        msg = ExecutionMessage("No applicable model definitions to generate a component diagram.", MessageLevel.INFO, None, None)
        messages.append(msg)
        return None, ExecutionResult(plugin_name, "puml-component", ExecutionStatus.GENERAL_FAILURE, messages)

    status = ExecutionStatus.SUCCESS
    msg = ExecutionMessage(
        f"Wrote PUML Component Diagram(s) to {output_directory}/.",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return new_file, ExecutionResult(plugin_name, "puml-component", status, messages)


def after_puml_component_generate(architecture_file: str, output_directory: str, run_generate: Callable
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-component command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_generate (Callable): Callback reference to the run_reference method from the Generate plugin.

    Returns:
        The results of the execution of the check command.
    """
    arch_file_content, execution_status = puml_component(architecture_file, output_directory)

    puml_component_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/component_diagram_generator.aac")
    )
    return run_generate(
        aac_plugin_file=arch_file_content,
        generator_file=puml_component_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_sequence_check(architecture_file: str, run_check: Callable) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_sequence(architecture_file: str, output_directory: str, classification: Optional[str]) -> tuple[str, ExecutionResult]:
    """
    Business logic for allowing puml-sequence command to perform the conversion of an AaC-defined use case to PlantUML sequence diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (Optional[str]): The level of classification for the output diagram file, or none if not provided.

    Returns:
        The YAML string to use in generating the output sequence diagram(s).
        ExecutionResult of the puml-sequence command for the PUML plugin.
    """
    # Initialize ExecutionResult for the puml-sequence command
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    # Parse the input file to extract the definitions to sort
    parsed_definitions: list[Definition] = parse(architecture_file)

    # Sort definition data into required data
    classification = classification.upper()
    use_case_data = sort_use_case_components(parsed_file=parsed_definitions,
                                             classification=classification)

    # Take a single use case at a time to extract participant and step data in the form of a list of strings
    yaml_list = []
    for use_case in use_case_data:
        yaml_list.append([{"usecase": use_case}])

    # Concatenate data definitions into a single string in yaml format
    new_file = ""
    for yaml_object in yaml_list:
        new_file = new_file + yaml.safe_dump_all(yaml_object, default_flow_style=False, sort_keys=False, explicit_start=True)

    # Check for if the passed file actually contained use case definitions and update ExecutionResult
    if len(use_case_data) < 1:
        msg = ExecutionMessage(
            "No applicable use case definitions to generate a sequence diagram.",
            MessageLevel.ERROR,
            None,
            None,
        )
        messages.append(msg)
        return None, ExecutionResult(plugin_name, "puml-sequence", ExecutionStatus.GENERAL_FAILURE, messages)

    status = ExecutionStatus.SUCCESS
    msg = ExecutionMessage(
        f"Wrote PUML Sequence Diagram(s) to {output_directory}",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return new_file, ExecutionResult(plugin_name, "puml-sequence", status, messages)


def after_puml_sequence_generate(architecture_file: str, output_directory: str, run_generate: Callable
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which to
                                 generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_generate (Callable): Callback reference to the run_generate method from the Generate plugin.

    Returns:
        The results of the execution of the generate command.
    """
    puml_sequence_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/sequence_diagram_generator.aac")
    )
    arch_file_content, execution_status = puml_sequence(architecture_file=architecture_file, output_directory=output_directory, classification=classification)

    return run_generate(
        aac_plugin_file=arch_file_content,
        generator_file=puml_sequence_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_object_check(architecture_file: str, run_check: Callable) -> ExecutionResult:
    """
    Run the Check AaC  command before the puml-object command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_object(architecture_file: str, output_directory: str, classification: Optional[str]) -> tuple[str, ExecutionResult]:
    """
    Business logic for allowing puml-object command to perform the conversion an AaC-defined system to PlantUML object diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (Optional[str]): The level of classification for the output diagram file, or none if not provided.

    Returns:
        The YAML string to use in generating the output object diagram(s).
        ExecutionResult of the puml-object command for the PUML plugin.
    """
    # Initialize ExecutionResult for the puml-component command
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    # Parse the input file to extract the definitions to sort
    parsed_file = parse(architecture_file)

    # Sort definitions into required data
    classification = classification.upper()
    object_data = get_object_data(parsed_file, classification)  # gets back a list of dictionaries containing a list of object_declarations, and a list of object hierarchies

    # Create a List of strings containing the sorted data definitions
    yaml_list = []
    for model in object_data:
        yaml_list.append([{"model": model}])

    # Concatenate data definitions into a single string in yaml format
    new_file = ""
    for yaml_object in yaml_list:
        new_file = new_file + yaml.safe_dump_all(yaml_object, default_flow_style=False, sort_keys=False, explicit_start=True)

    # Check for if the passed data actually contained model definitions and update ExecutionResult
    if len(object_data) < 1:
        msg = ExecutionMessage(
            "No applicable model definitions to generate an object diagram.",
            MessageLevel.INFO,
            None,
            None,
        )
        messages.append(msg)
        return None, ExecutionResult(plugin_name, "puml-object", ExecutionStatus.GENERAL_FAILURE, messages)

    status = ExecutionStatus.SUCCESS
    msg = ExecutionMessage(
        f"Wrote PUML Object Diagram(s) to {output_directory}",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return new_file, ExecutionResult(plugin_name, "puml-object", status, messages)


def after_puml_object_generate(architecture_file: str, output_directory: str, run_generate: Callable) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-object command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_generate (Callable): Callback reference to the run_generate method from the Generate plugin.

    Returns:
        The results of the execution of the generate command.
    """
    arch_file_content, execution_status = puml_object(architecture_file, output_directory)

    puml_object_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/object_diagram_generator.aac")
    )
    return run_generate(
        aac_plugin_file=arch_file_content,
        generator_file=puml_object_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_requirements_check(architecture_file: str, run_check: Callable) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-requirements command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_requirements(architecture_file: str, output_directory: str, classification: Optional[str]) -> tuple[str, ExecutionResult]:
    """
    Business logic for allowing puml-requirements command to perform the conversion of an AaC-defined system to a requirements diagram in PlantUML format.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (Optional[str]): The level of classification for the output diagram file, or none if not provided.

    Returns:
        The YAML string to use in generating the output requirements diagram(s).
        The results of the execution of the puml-requirements command.
    """
    # Initialize ExecutionResult for the puml-sequence command
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    # Establish necessary data holders for sorting through the definitions
    req_spec_definitions: dict = {}
    req_definitions: dict = {}

    # Parse the input file to extract the definitions to sort
    parsed_definitions: list[Definition] = parse(architecture_file)

    # Sort through the parsed definitions into their top level categories
    for definition in parsed_definitions:
        if definition.get_root_key() == "req_spec":
            req_spec_definitions[definition.name] = definition
        if definition.get_root_key() == "req":
            req_definitions[definition.name] = definition

    classification = classification.upper()
    requirement_data = get_requirements_defs(req_definitions, classification)

    # Create a List of strings containing the sorted data definitions
    yaml_list = []
    for req in requirement_data:
        yaml_list.append([{"req_spec": req}])

    # Concatenate data definitions into a single string in yaml format
    new_file = ""
    for yaml_object in yaml_list:
        new_file = new_file + yaml.safe_dump_all(yaml_object, default_flow_style=False, sort_keys=False, explicit_start=True)

    # Check for if the passed file actually contained req_spec definitions and update ExecutionResult
    if len(req_spec_definitions) < 1:
        msg = ExecutionMessage(
            "No applicable requirement specification definitions to generate a requirements diagram.",
            MessageLevel.ERROR,
            None,
            None,
        )
        messages.append(msg)
        return None, ExecutionResult(plugin_name, "puml-requirements", status, messages)

    status = ExecutionStatus.SUCCESS
    msg = ExecutionMessage(
        f"Wrote PUML Requirements Diagram(s) to {output_directory}",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return new_file, ExecutionResult(plugin_name, "puml-requirements", status, messages)


def after_puml_requirements_generate(architecture_file: str, output_directory: str, run_generate: Callable) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-requirements command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.

        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_generate (Callable): Callback reference to the run_generate method from the Generate plugin.

    Returns:
        The results of the execution of the generate command.
    """
    puml_requirements_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/requirements_diagram_generator.aac")
    )
    arch_file_content, result = puml_requirements(architecture_file, output_directory)
    return run_generate(
        aac_plugin_file=arch_file_content,
        generator_file=puml_requirements_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )
