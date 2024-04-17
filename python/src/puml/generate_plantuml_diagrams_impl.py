"""The AaC Generate PlantUML Diagrams plugin implementation module."""

# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
import yaml

from os import path, remove
from typing import Callable

# from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
    MessageLevel,
)
from aac.in_out.writer import write_file
from aac.in_out.parser._parse_source import parse

from .helpers.sequence_helpers import _get_use_case_participants, _get_use_case_steps

plugin_name = "Generate PlantUML Diagrams"


def before_puml_component_check(
    architecture_file: str, output_directory: str, run_check: Callable
) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-component command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_component(architecture_file: str, output_directory: str) -> ExecutionResult:
    """
    Business logic for allowing puml-component command to perform the conversion of an AaC-defined system to a PlantUML component diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        results of the execution of the puml-component command.
    """
    messages = []

    status = ExecutionStatus.SUCCESS
    msg = ExecutionMessage(
        f"Wrote PUML Component Diagram(s) to {output_directory}/.",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return ExecutionResult(plugin_name, "puml-sequence", status, messages)


def after_puml_component_generate(
    architecture_file: str, output_directory: str, run_generate: Callable
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

    puml_component_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/component_diagram_generator.aac")
    )
    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_component_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_sequence_check(
    architecture_file: str, output_directory: str, classification: str, run_check: Callable
) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (str): The level of classification for the output diagram file.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_sequence(architecture_file: str, output_directory: str, classification: str) -> tuple[list[str], ExecutionResult]:
    """
    Business logic for allowing puml-sequence command to perform the conversion of an AaC-defined use case to PlantUML sequence diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (str): The level of classification for the output diagram file.

    Returns:
        sequence_files (list[str]): The list of sequence yaml file(s) to use in generating the output sequence diagram(s).
        ExecutionResult of the puml-sequence command for the PUML plugin.
    """
    # Initialize ExecutionResult for the puml-sequence command
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    # Establish necessary data holders for sorting through the definitions
    use_case_definitions: dict = {}
    use_case_actors: dict = {}
    use_case_steps: dict = {}
    properties: dict = {}
    sequence_files: list[str] = []

    # Parse the input file to extract the definitions to sort
    parsed_definitions: list[Definition] = parse(architecture_file)

    # Sort through the parsed definitions into their top level categories
    for definition in parsed_definitions:
        if definition.get_root_key() == "usecase":
            use_case_definitions[definition.name] = definition
        if definition.get_root_key() == "actor":
            use_case_actors[definition.name] = definition
        if definition.get_root_key() == "usecase_step":
            use_case_steps[definition.name] = definition

    # Take a single use case at a time to extract participant and step data
    for use_case_definition in use_case_definitions:
        use_case_title = use_case_definitions[use_case_definition].name
        use_case = use_case_definitions[use_case_definition].structure["usecase"]

        participants = _get_use_case_participants(use_case=use_case, use_case_actors=use_case_actors)
        sequences = _get_use_case_steps(use_case=use_case, use_case_steps=use_case_steps)

        properties["usecase"] = {
            "name": use_case_title,
            "participants": participants,
            "sequences": sequences,
            "classification": classification
        }

        # Write use case data to new temp file for populating the diagram from in generate
        new_sequence_file = path.abspath(path.join(path.dirname(__file__), f"./{use_case_title}_sequence_diagram_content.yaml"))
        properties_yaml = yaml.dump(properties, default_flow_style=False)
        write_file(uri=new_sequence_file, content=properties_yaml, overwrite=True)

        sequence_files.append(new_sequence_file)

    # Check for if the passed file actually contained use case definitions and update ExecutionResult
    if len(use_case_definitions) > 0:
        status = ExecutionStatus.SUCCESS
        msg = ExecutionMessage(
            f"Wrote PUML Sequence Diagram(s) to {output_directory}",
            MessageLevel.INFO,
            None,
            None,
        )
    else:
        msg = ExecutionMessage(
            "No applicable use case definitions to generate a sequence diagram.",
            MessageLevel.ERROR,
            None,
            None,
        )
    messages.append(msg)

    return sequence_files, ExecutionResult(plugin_name, "puml-sequence", status, messages)


def after_puml_sequence_generate(
    architecture_file: str, output_directory: str, classification: str, run_generate: Callable
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which to
                                 generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        classification (str): The level of classification for the output diagram file.
        run_generate (Callable): Callback reference to the run_generate method from the Generate plugin.

    Returns:
        The results of the execution of the generate command.
    """
    puml_sequence_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/sequence_diagram_generator.aac")
    )
    sequence_files, execution_status = puml_sequence(architecture_file=architecture_file, output_directory=output_directory,
                                                     classification=classification)

    for sequence_file in sequence_files:
        generate_result = run_generate(aac_plugin_file=sequence_file,
                                       generator_file=puml_sequence_generator_file,
                                       code_output=output_directory,
                                       test_output="",
                                       doc_output="",
                                       no_prompt=True,
                                       force_overwrite=True,
                                       evaluate=False,
                                       )
        remove(sequence_file)
    return generate_result


def before_puml_object_check(
    architecture_file: str, output_directory: str, run_check: Callable
) -> ExecutionResult:
    """
    Run the Check AaC  command before the puml-object command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_object(architecture_file, output_directory) -> ExecutionResult:
    """
    Business logic for allowing puml-object command to perform the conversion an AaC-defined system to PlantUML object diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the puml-object command.
    """

    # TODO: implement plugin logic here
    status = ExecutionStatus.SUCCESS
    messages: list[ExecutionMessage] = []
    msg = ExecutionMessage(
        f"Wrote PUML Object Diagram(s) to {output_directory}",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return ExecutionResult(plugin_name, "puml-object", status, messages)


def after_puml_object_generate(
    architecture_file: str, output_directory: str, run_generate: Callable
) -> ExecutionResult:
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
    puml_object_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/object_diagram_generator.aac")
    )
    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_object_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_requirements_check(
    architecture_file: str, output_directory: str, run_check: Callable
) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-requirements command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.
        run_check (Callable): Callback reference to the run_check method from the Check plugin.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_requirements(architecture_file, output_directory) -> ExecutionResult:
    """
    Business logic for allowing puml-requirements command to perform the conversion of an AaC-defined system to a requirements diagram in PlantUML format.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the puml-requirements command.
    """

    # TODO: implement plugin logic here
    status = ExecutionStatus.SUCCESS
    messages: list[ExecutionMessage] = []
    msg = ExecutionMessage(
        f"Wrote PUML Requirement Diagram(s) to {output_directory}",
        MessageLevel.INFO,
        None,
        None,
    )
    messages.append(msg)

    return ExecutionResult(plugin_name, "puml-requirements", status, messages)


def after_puml_requirements_generate(
    architecture_file: str, output_directory: str, run_generate: Callable
) -> ExecutionResult:
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
    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_requirements_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=True,
        force_overwrite=True,
        evaluate=False,
    )
