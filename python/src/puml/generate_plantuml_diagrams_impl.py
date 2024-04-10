"""The AaC Generate PlantUML Diagrams plugin implementation module."""

# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.

# There may be some unused imports depending on the definition of the plugin...but that's ok
from os import path
from typing import Any

from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
    MessageLevel,
)
from aac.in_out.parser._parse_source import parse

plugin_name = "Generate PlantUML Diagrams"
COMPONENT_STRING = "component"
OBJECT_STRING = "object"
SEQUENCE_STRING = "sequence"
REQUIREMENTS_STRING = "requirements"


# def _model_sort(models: List[dict]) -> List[dict]:
#     context = LanguageContext()
#     for model in models:
#         if model.get_root_key() == "model":
#             model_name = model.name
#             model_inputs = []
#             for input in model.structure["model"]["behavior"]["input"]:
#                 input_name = input.name
#                 input_type = input.type
#                 model_inputs.append({"name": input_name, "type" : input_type, "target": model_name})
#             model_outputs = []
#             for output in model.structure["model"]["behavior"]["output"]:
#                 output_name = output.name
#                 output_type = output.type
#                 model_outputs.append({"name": output_name, "type": output_type, "source": model_name})
#             model_components = []
#             for component in model.structure["model"]["components"]:
#                 component_type = component.type
#                 model_components.append(_model_sort(context.get_definitions_by_name(component_type), diagram_type, archfile_path))
#             definitions.append({"name": model_name, "interfaces": model_interfaces, "components": model_components, "inputs": model_inputs, "outputs": model_outputs})
#     return definitions


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
    """
    Business logic for allowing puml-component command to perform the conversion of an AaC-defined system to a PlantUML component diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The definition contents as a list
    """
    messages = []
    architecture_file_path = path.abspath(architecture_file)
    parsed_file = parse(architecture_file)

    # component_data = _model_sort(parsed_file)

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
    architecture_file: str, output_directory: str, run_generate
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-component command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML component diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the check command.
    """

    code = output_directory
    # arch_file_content = puml_component(architecture_file, output_directory)

    puml_component_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/component_diagram_generator.aac")
    )
    return run_generate(
        architecture_file,
        puml_component_generator_file,
        code,
        "",
        "",
        True,
        True,
        False,
    )


def before_puml_sequence_check(
    architecture_file: str, output_directory: str, run_check: Any
) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the check command.
    """
    return run_check(architecture_file, False, False)


def puml_sequence(architecture_file: str, output_directory: str) -> tuple[dict, ExecutionResult]:
    """
    Business logic for allowing puml-sequence command to perform the conversion of an AaC-defined use case to PlantUML sequence diagram.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which
                                 to generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        properties (dict): The sorted use case definition components to use in generating the output sequence diagram.
        ExecutionResult of the puml-sequence command for the PUML plugin.
    """
    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    parsed_definitions: list = parse(architecture_file)
    use_case_definitions: dict = {}
    use_case_actors: dict = {}
    use_case_steps: dict = {}
    properties: dict = {}

    for definition in parsed_definitions:
        if definition.get_root_key() == "usecase":
            use_case_definitions[definition.name] = definition
        if definition.get_root_key() == "actor":
            use_case_actors[definition.name] = definition
        if definition.get_root_key() == "usecase_step":
            use_case_steps[definition.name] = definition

    for use_case_definition in use_case_definitions:
        use_case_title = use_case_definitions[use_case_definition].name
        use_case = use_case_definitions[use_case_definition].structure["usecase"]

    participants = _get_use_case_participants(use_case=use_case, use_case_actors=use_case_actors)
    sequences = _get_use_case_steps(use_case=use_case, use_case_steps=use_case_steps)

    properties = {"usecase": {
        "title": use_case_title,
        "participants": participants,
        "sequences": sequences}
    }

    messages.append(ExecutionMessage(f"use case properties: {properties}", MessageLevel.INFO, None, None))

    if len(use_case_definitions) > 0:
        status = ExecutionStatus.SUCCESS
        msg = ExecutionMessage(
            f"Wrote PUML Sequence Diagram(s) to {output_directory}/.",
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

    return properties, ExecutionResult(plugin_name, "puml-sequence", status, messages)


def _get_use_case_participants(use_case: Any, use_case_actors: dict) -> list[dict]:
    """
    Helper method for extracting the participants from a use case definition.

    Args:
        use_case (Any): The use case definition from which to extract participants.
        use_case_actors (dict): The dictionary of actors within the use case definition.

    Returns:
        The list of participants and their data within the use case definition.
    """
    participants: list[dict] = []

    # declare participants
    use_case_participants = use_case["participants"]
    for use_case_participant in use_case_participants:  # each participant is a field type
        if use_case_participant in use_case_actors.keys():
            participant = use_case_actors[use_case_participant].structure["actor"]
            if "model" in participant.keys():
                participants.append(
                    {
                        "type": participant["model"],
                        "name": participant["name"],
                    }
                )
            else:
                participants.append(
                    {
                        "type": "External",
                        "name": participant["name"],
                    }
                )
    return participants


def _get_use_case_steps(use_case: Any, use_case_steps: dict) -> list[dict]:
    """
    Helper method for extracting the participants from a use case definition.

    Args:
        use_case (Any): The use case definition from which to extract participants.
        use_case_steps (dict): The dictionary of steps within the use case definition.
    Returns:
        The list of participants and their data within the use case definition.
    """
    sequences: list[dict] = []

    # process steps
    steps = use_case["steps"]
    for step in steps:  # each step of a step type
        if step in use_case_steps.keys():
            use_case_step = use_case_steps[step].structure["usecase_step"]
        sequences.append(
            {
                "name": use_case_step["name"],
                "source": use_case_step["source"],
                "target": use_case_step["target"],
                "action": use_case_step["action"],
            }
        )

    return sequences


def after_puml_sequence_generate(
    architecture_file: str, output_directory: str, run_generate: Any
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-sequence command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined use case from which to
                                 generate a PlantUML sequence diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the generate command.
    """
    puml_sequence_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/sequence_diagram_generator.aac")
    )

    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_sequence_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=False,
        force_overwrite=True,
        evaluate=False,
    )


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
    error_msg = ExecutionMessage(
        "The puml-object command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-object", status, messages)


def after_puml_object_generate(
    architecture_file: str, output_directory: str, run_generate: Any
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-object command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML object diagram.
        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the generate command.
    """
    puml_object_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/object_generator.aac")
    )
    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_object_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=False,
        force_overwrite=True,
        evaluate=False,
    )


def before_puml_requirements_check(
    architecture_file: str, output_directory: str, run_check
) -> ExecutionResult:
    """
    Run the Check AaC command before the puml-requirements command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.

        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

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
    error_msg = ExecutionMessage(
        "The puml-requirements command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
        MessageLevel.ERROR,
        None,
        None,
    )
    messages.append(error_msg)

    return ExecutionResult(plugin_name, "puml-requirements", status, messages)


def after_puml_requirements_generate(
    architecture_file: str, output_directory: str, run_generate: Any
) -> ExecutionResult:
    """
    Run the Generate generate command after the puml-requirements command.

    Args:
        architecture_file (str): A path to a YAML file containing an AaC-defined system from which to
                                 generate a PlantUML requirements diagram.

        output_directory (str): The output directory into which the PlantUML (.puml) diagram file
                                will be written.

    Returns:
        The results of the execution of the generate command.
    """
    puml_requirements_generator_file = path.abspath(
        path.join(path.dirname(__file__), "./generators/requirements_generator.aac")
    )
    return run_generate(
        aac_plugin_file=architecture_file,
        generator_file=puml_requirements_generator_file,
        code_output=output_directory,
        test_output="",
        doc_output="",
        no_prompt=False,
        force_overwrite=True,
        evaluate=False,
    )
