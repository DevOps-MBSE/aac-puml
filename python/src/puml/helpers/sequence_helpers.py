"""
Helper methods for extracting pertinent use case definition data for use in generating
sequence diagrams in a PUML format.
"""
from typing import Any


def get_use_case_participant(use_case: Any, use_case_actor: dict) -> str:
    """
    Helper method for extracting the matching participant information from a use case definition.

    Args:
        use_case (Any): The use case definition from which to extract participants.
        use_case_actor (dict): The actor definition for a use case participant to match against.

    Returns:
        The participant actor model information.
    """
    # declare participants
    use_case_participants = use_case["participants"]
    for use_case_participant in use_case_participants:  # each participant is a field type
        if use_case_participant in use_case_actor.keys():
            participant = use_case_actor.structure["actor"]
            if "model" in participant.keys():
                return f"{participant['type']} as {participant['name']}"
            else:
                return f"External as {participant['name']}"


def get_use_case_step(use_case: Any, use_case_step: dict) -> str:
    """
    Helper method for extracting the matching step information from a use case definition.

    Args:
        use_case (Any): The use case definition from which to extract the steps.
        use_case_step (dict): The dictionary of a use case step to match against.
    Returns:
        The use case step model information.
    """
    sequences: list[dict] = []

    # process steps
    steps = use_case["steps"]
    for step in steps:  # each step of a step type
        if step in use_case_step.keys():
            use_case_step = use_case_step.structure["usecase_step"]
        sequences.append(
            {
                "name": use_case_step["name"],
                "source": use_case_step["source"],
                "target": use_case_step["target"],
                "action": use_case_step["action"],
            }
        )

    return sequences
