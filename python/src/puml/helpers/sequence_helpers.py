"""
Helper methods for extracting pertinent use case definition data for use in generating
sequence diagrams in a PUML format.
"""


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
