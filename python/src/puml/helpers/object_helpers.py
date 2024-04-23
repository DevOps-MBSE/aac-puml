"""
Helper methods for extracting and sorting pertinent model data for use in generating
object diagrams in a PUML format.
"""


def get_object_data(models: list[dict]) -> list[dict]:
    """
    Helper method for extracting data from a model

    Args:
        models (List[dict]): A list of model definitions

    Returns:
        A list of dictionaries of organized data for diagram generation
    """
    definitions = []
    for model in models:
        object_declarations = []
        object_compositions = {}
        model_dict = {}
        if model.get_root_key() == "model":
            model_name = model.name
            object_declarations.append(model_name)
            if "components" in model.content:
                for component in model.structure["model"]["components"]:
                    if model_name not in object_compositions:
                        object_compositions[model_name] = set()

                    object_compositions.get(model_name, set()).add(component["model"])

                object_hierarchies = []
                for parent in object_compositions:
                    for child in object_compositions.get(parent, set()):
                        object_hierarchies.append({"parent": parent, "child": child})
            model_dict["name"] = model_name
            model_dict["objects"] = object_declarations
            model_dict["object_hierarchies"] = object_hierarchies

            definitions.append(model_dict)
    return definitions
