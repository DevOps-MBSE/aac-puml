"""
Helper methods for extracting pertinent use case definition data for use in generating
sequence diagrams in a PUML format.
"""
from aac.context.definition import Definition


def sort_use_case_components(parsed_file: list[Definition]) -> list[dict]:
    """
    Helper method for sorting the use case definition into its components.

    Args:
        parsed_file (list[Definition]): The list of definitions from the parsed file to sort through.

    Returns:
        The list of use case components to use for populating the sequence diagram.
    """
    # Establish necessary data holders for sorting through the definitions
    use_case_definitions: dict = {}
    use_case_actors: dict = {}
    use_case_steps: dict = {}
    properties: list = []

    # Sort through the parsed definitions into their top level categories
    for definition in parsed_file:
        if definition.get_root_key() == "usecase":
            use_case_definitions[definition.name] = definition
        if definition.get_root_key() == "actor":
            use_case_actors[definition.name] = definition
        if definition.get_root_key() == "usecase_step":
            use_case_steps[definition.name] = definition

    # Take a single use case at a time to extract participant and step data in the form of a list of strings
    for use_case_definition in use_case_definitions:
        use_case_title = use_case_definitions[use_case_definition].name
        use_case = use_case_definitions[use_case_definition].structure["usecase"]

        participants = _get_use_case_participants(use_case=use_case, use_case_actors=use_case_actors)
        sequences = _get_use_case_steps(use_case=use_case, use_case_steps=use_case_steps)

        use_case_dict: dict = {}
        use_case_dict["name"] = use_case_title
        use_case_dict["participants"] = participants
        use_case_dict["sequences"] = sequences
        properties.append(use_case_dict)

    return properties


def _get_use_case_participants(use_case: dict, use_case_actors: dict) -> list[dict]:
    """
    Helper method for extracting the participants from a use case definition.

    Args:
        use_case (dict): The use case definition from which to extract participants.
        use_case_actors (dict): The dictionary of actors associated with the use case definition.

    Returns:
        The list of participants and their data within the use case definition.
    """
    participants: list[dict] = []

    use_case_participants = use_case["participants"]
    for use_case_participant in use_case_participants:
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


def _get_use_case_steps(use_case: dict, use_case_steps: dict) -> list[dict]:
    """
    Helper method for extracting the steps associated with a use case definition.

    Args:
        use_case (dict): The use case definition from which to extract steps.
        use_case_steps (dict): The dictionary of steps associated with the use case definition.
    Returns:
        The list of steps and their data associated with the use case definition.
    """
    sequences: list[dict] = []

    steps = use_case["steps"]
    for step in steps:
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
