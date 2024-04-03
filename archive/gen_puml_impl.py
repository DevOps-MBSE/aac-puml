"""The AaC Generate PlantUML Diagrams plugin implementation module."""
# NOTE: It is safe to edit this file.
# This file is only initially generated by aac gen-plugin, and it won't be overwritten if the file already exists.
from os import path, makedirs
from typing import Any

# There may be some unused imports depending on the definition of the plugin...but that's ok
from aac.execute.aac_execution_result import (
    ExecutionResult,
    ExecutionStatus,
    ExecutionMessage,
    MessageLevel,
)
from aac.in_out.files.aac_file import AaCFile
from aac.in_out.parser._parse_source import parse
from aac.context.language_context import LanguageContext
from aac.context.definition import Definition
from aac.context.source_location import SourceLocation


from puml.puml_helpers import (
    generate_diagram_to_file,
    get_model_content,
    get_generated_file_name,
    extract_aac_file_name,
)


plugin_name = "Generate PlantUML Diagrams"
COMPONENT_STRING = "component"
OBJECT_STRING = "object"
SEQUENCE_STRING = "sequence"
REQUIREMENTS_STRING = "requirements"


def puml_component(architecture_file: str, output_directory: str) -> ExecutionResult:
    """
    Convert an AaC model to Plant UML component diagram.

    Args:
        architecture_file (str): Path to a yaml file containing an AaC usecase from which to generate a Plant UML component diagram.
        output_directory (str): Output directory for the PlantUML (.puml) diagram file.
    """
    architecture_file_path = path.abspath(architecture_file)
    parsed_file = parse(architecture_file)

    status = ExecutionStatus.GENERAL_FAILURE
    messages: list[ExecutionMessage] = []

    def _generate_component_diagram(definitions: list[Definition]):
        for definition in parsed_file:
            if definition.get_root_key() == "model":
                models = []
                model_name = definition.name
                model_properties = get_model_content(definition, set())
                aac_file_name = extract_aac_file_name(architecture_file)
                generated_file_name = get_generated_file_name(aac_file_name, COMPONENT_STRING, model_name, output_directory)
                models.append(
                    {
                        "filename": generated_file_name,
                        "title": model_name,
                        "models": [model_properties],
                    }
                )
            return models

    try:
        generate_to_file = generate_diagram_to_file(architecture_file_path=architecture_file_path,
                                               output_directory=output_directory,
                                               puml_type=COMPONENT_STRING,
                                               property_generator=_generate_component_diagram)
        generation_result_msg = ExecutionMessage(
            generate_to_file,
            MessageLevel.INFO,
            None,
            None,
        )

    except Exception:
        generation_result_msg = ExecutionMessage(
            "The puml-component command for the Generate PlantUML Diagrams plugin has not been implemented yet.",
            MessageLevel.ERROR,
            None,
            None,
        )

    messages.append(generation_result_msg)





    with plugin_result(
        plugin_name,
        generate_diagram_to_file,
        architecture_file_path,
        output_directory,
        COMPONENT_STRING,
        _generate_component_diagram,
    ) as result:
        return result



    return ExecutionResult(plugin_name, "puml-component", status, messages)

# ----------------------------------
#   LEGACY REFERENCE CODE
# ----------------------------------
# def puml_component(architecture_file: str, output_directory: str) -> PluginExecutionResult:
#     """
#     Convert an AaC model to Plant UML component diagram.

#     Args:
#         architecture_file (str): Path to a yaml file containing an AaC usecase from which to generate a Plant UML component diagram.
#         output_directory (str): Output directory for the PlantUML (.puml) diagram file.
#     """
#     architecture_file_path = os.path.abspath(architecture_file)

#     def generate_component_diagram(definitions: list[Definition]):
#         model_definitions = get_definitions_by_root_key("model", definitions)

#         models = []
#         for model_definition in model_definitions:
#             root_model_name = model_definition.name
#             model_properties = get_model_content(model_definition, set())
#             aac_file_name = extract_aac_file_name(architecture_file)
#             generated_file_name = get_generated_file_name(aac_file_name, COMPONENT_STRING, root_model_name, output_directory)
#             models.append(
#                 {
#                     "filename": generated_file_name,
#                     "title": model_definition.name,
#                     "models": [model_properties],
#                 }
#             )

#         return models

#     with plugin_result(
#         plugin_name,
#         generate_diagram_to_file,
#         architecture_file_path,
#         output_directory,
#         COMPONENT_STRING,
#         generate_component_diagram,
#     ) as result:
#         return result


def puml_sequence(architecture_file: str, output_directory: str) -> ExecutionResult:
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

# ----------------------------------
#   LEGACY REFERENCE CODE
# ----------------------------------
# def puml_sequence(architecture_file: str, output_directory: str) -> PluginExecutionResult:
#     """
#     Convert an AaC usecase to Plant ULM sequence diagram.

#     Args:
#         architecture_file: str: Path to a yaml file containing an AaC usecase from which to generate a Plant UML sequence diagram.
#         output_directory (str): Output directory for the PlantUML (.puml) diagram file (optional)
#     """
#     architecture_file_path = os.path.abspath(architecture_file)

#     def generate_sequence_diagram(definitions: list[Definition]):
#         usecase_definitions = get_definitions_by_root_key("usecase", definitions)

#         properties = []

#         for usecase_definition in usecase_definitions:
#             participants = []
#             sequences = []

#             use_case_title = usecase_definition.name
#             # declare participants
#             usecase_participants = search_definition(usecase_definition, ["usecase", "participants"])
#             for usecase_participant in usecase_participants:  # each participant is a field type
#                 participants.append(
#                     {
#                         "type": usecase_participant.get("type"),
#                         "name": usecase_participant.get("name"),
#                     }
#                 )

#             # process steps
#             steps = search_definition(usecase_definition, ["usecase", "steps"])
#             for step in steps:  # each step of a step type
#                 sequences.append(
#                     {
#                         "source": step.get("source"),
#                         "target": step.get("target"),
#                         "action": step.get("action"),
#                     }
#                 )

#             aac_file_name = extract_aac_file_name(architecture_file)
#             generated_file_name = get_generated_file_name(aac_file_name, SEQUENCE_STRING, use_case_title, output_directory)
#             properties.append(
#                 {
#                     "filename": generated_file_name,
#                     "title": use_case_title,
#                     "participants": participants,
#                     "sequences": sequences,
#                 }
#             )

#         return properties

#     with plugin_result(
#         plugin_name,
#         generate_diagram_to_file,
#         architecture_file_path,
#         output_directory,
#         SEQUENCE_STRING,
#         generate_sequence_diagram,
#     ) as result:
#         return result


def puml_object(architecture_file: str, output_directory: str) -> ExecutionResult:
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

# ----------------------------------
#   LEGACY REFERENCE CODE
# ----------------------------------
# def puml_object(architecture_file: str, output_directory: str) -> PluginExecutionResult:
#     """
#     Convert an AaC model to Plant ULM object diagram.

#     Args:
#         architecture_file: str: Path to a yaml file containing an AaC usecase from which to generate a Plant UML object diagram.
#         output_directory (str): Output directory for the PlantUML (.puml) diagram file (optional)
#     """
#     architecture_file_path = os.path.abspath(architecture_file)

#     def generate_object_diagram(definitions: list[Definition]):
#         model_definitions = get_definitions_by_root_key("model", definitions)

#         object_declarations = []
#         object_compositions = {}
#         for model_definition in model_definitions:
#             model_name = model_definition.name
#             object_declarations.append(model_name)

#             for component in search_definition(model_definition, ["model", "components", "type"]):
#                 if model_name not in object_compositions:
#                     object_compositions[model_name] = set()

#                 object_compositions.get(model_name, set()).add(component)

#         object_hierarchies = []
#         for parent in object_compositions:
#             for child in object_compositions.get(parent, {}):
#                 object_hierarchies.append({"parent": parent, "child": child})

#         aac_file_name = extract_aac_file_name(architecture_file)
#         generated_filename = get_generated_file_name(aac_file_name, OBJECT_STRING, model_name, output_directory)
#         return [
#             {
#                 "filename": generated_filename,
#                 "objects": object_declarations,
#                 "object_hierarchies": object_hierarchies,
#             }
#         ]

#     with plugin_result(
#         plugin_name,
#         generate_diagram_to_file,
#         architecture_file_path,
#         output_directory,
#         OBJECT_STRING,
#         generate_object_diagram,
#     ) as result:
#         return result


def puml_requirements(architecture_file: str, output_directory: str) -> ExecutionResult:
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

# ----------------------------------
#   LEGACY REFERENCE CODE
# ----------------------------------
# def puml_requirements(architecture_file: str, output_directory: str) -> PluginExecutionResult:
#     """
#     Generate a requirements diagram from the requirements of a system modeled with AaC.

#     Args:
#         architecture_file (str): Path to an AaC file containing modeled requirements from which to generate a requirements diagram.
#         output_directory (str): Output directory for the PlantUML (.puml) diagram file.
#     """
#     architecture_file_path = os.path.abspath(architecture_file)

#     def _generate_requirements_diagram(definitions: list[Definition]):
#         return generate_requirements_diagram(architecture_file, output_directory, definitions)

#     with plugin_result(
#         plugin_name,
#         generate_diagram_to_file,
#         architecture_file_path,
#         output_directory,
#         REQUIREMENTS_STRING,
#         _generate_requirements_diagram,
#     ) as result:
#         return result