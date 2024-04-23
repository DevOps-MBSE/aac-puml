"""
Helper methods for extracting and sorting pertinent model data for use in generating
component diagrams in a PUML format.
"""
from aac.context.language_context import LanguageContext
from aac.context.definition import Definition


def _input_sort(model: Definition, defined_interfaces: set, model_interfaces: set) -> tuple[set, set, list[dict]]:
    """
    Method to extract input information from a model

    Args:
        model (Definition): The model containing the desired input data
        defined_interfaces (set): A set of all the input and output types from all given models
        model_interfaces (set): A set of all the input and output types from just the current model

    Returns:
        defined_interfaces (set): A set of all the input and output types from all given models
        model_interfaces (set): A set of all the input and output types from just the current model
        A List of inputs from the model
    """
    model_inputs = []
    for behavior in model.structure["model"]["behavior"]:
        for input in behavior["input"]:
            input_name = input["name"]
            input_type = input["type"]
            model_inputs.append({"name": input_name, "type": input_type, "target": model.name})
            if input_type not in defined_interfaces:
                defined_interfaces.add(input_type)
                model_interfaces.add(input_type)
    return defined_interfaces, model_interfaces, model_inputs


def _output_sort(model: Definition, defined_interfaces: set, model_interfaces: set) -> tuple[set, set, list[dict]]:
    """
    Method to extract output information from a model

    Args:
        model (Definition): The model containing the desired output data
        defined_interfaces (set): A set of all the input and output types from all given models
        model_interfaces (set): A set of all the input and output types from just the current model

    Returns:
        defined_interfaces (set): A set of all the input and output types from all given models
        model_interfaces (set): A set of all the input and output types from just the current model
        A List of outputs from the model
    """
    model_outputs = []
    for behavior in model.structure["model"]["behavior"]:
        if "output" in behavior:
            for output in behavior["output"]:
                output_name = output["name"]
                output_type = output["type"]
                model_outputs.append({"name": output_name, "type": output_type, "source": model.name})
                if output_type not in defined_interfaces:
                    defined_interfaces.add(output_type)
                    model_interfaces.add(output_type)
    return defined_interfaces, model_interfaces, model_outputs


def model_sort(models: list[dict], defined_interfaces: set) -> list[dict]:
    """
    Helper method for extracting and sorting data from a model

    Args:
        models (List[dict]): A list of model definitions
        defined_interfaces (set): a set of all the input and output types.  Passed in as an empty set usually, but used in recursion.

    Returns:
        A List of dictionaries of organized data for diagram generation
    """
    context = LanguageContext()
    definitions = []
    for model in models:
        model_interfaces = set()
        model_dict = {}
        if model.get_root_key() == "model":
            model_name = model.name
            model_inputs = []
            model_dict["name"] = model_name
            if "input" in model.content:
                defined_interfaces, model_interfaces, model_inputs = _input_sort(model, defined_interfaces, model_interfaces)
                model_dict["inputs"] = model_inputs
            model_outputs = []
            defined_interfaces, model_interfaces, model_outputs = _output_sort(model, defined_interfaces, model_interfaces)
            model_dict["outputs"] = model_outputs
            model_components = []
            if "components" in model.content:
                for component in model.structure["model"]["components"]:
                    component_type = component["model"]
                    model_components.append(model_sort(models=context.get_definitions_by_name(component_type),
                                                       defined_interfaces=defined_interfaces)[0])
                model_dict["components"] = model_components
            if model_interfaces:
                model_dict["interfaces"] = list(model_interfaces)

            definitions.append(model_dict)
    return definitions
