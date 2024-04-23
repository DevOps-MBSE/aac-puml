"""
Helper methods for extracting and sorting pertinent model data for use in generating requirements
diagrams in a PUML format.
"""
from typing import Optional


def get_requirements_defs(reqs: dict) -> list[dict]:
    """
    Helper method for extracting and sorting data from a requirement specification.

    Args:
        reqs (dict): A dictionary of requirement definitions.

    Returns:
        A list of dictionaries of organized data for diagram generation.
    """
    requirements = []
    if reqs:
        for req_key in reqs:
            req_dict = {}
            req = reqs[req_key]
            id = req.structure["req"]["id"]
            attributes = req.structure["req"]["attributes"]
            tadi_type = _get_requirement_type(attributes)
            title = req.structure["req"]["name"]
            name = req.structure["req"]["name"]
            shall = req.structure["req"]["shall"]
            connected = _get_connected_requirements(req, reqs)

            req_dict["title"] = title
            req_dict["name"] = name
            req_dict["id"] = id
            req_dict["shall"] = shall
            req_dict["attributes"] = attributes
            req_dict["type"] = tadi_type
            req_dict["connected"] = connected

            requirements.append(req_dict)
    return requirements


def _get_requirement_type(attributes: list[dict]) -> str:
    """
    Helper method for extracting the TADI type of a requirement.

    Args:
        attributes (List[dict]): A List of a requirement definitions attributes.

    Returns:
        The value of the TADI attribute.
    """
    if not attributes:
        attributes = [{}]
    for attribute in attributes:
        if attribute["name"] == "TADI":
            return attribute["value"]


def _get_connected_requirements(req: dict, reqs: dict) -> list[dict]:
    """
    Helper method that finds the parent and child requirement definitions for a specified requirement.

    Args:
        req (dict): A requirement definition.
        reqs (dict): A dictionary containing all requirement definitions.

    Returns:
        A list of parent and child requirement definitions for the specified requirement.
    """
    connected_reqs = []

    for struct in reqs:
        if req != struct:
            req_id = req.structure["req"]["id"]

            child = _get_child_requirements(req_id, reqs[struct])
            if child:
                connected_reqs.append(child)

            parent = _get_parent_requirements(req_id, reqs[struct])
            if parent:
                connected_reqs.append(parent)
    return connected_reqs


def _get_child_requirements(req_id: str, other_req: dict) -> Optional[dict]:
    """
    Helper method that calls _get_requirement_ancestry() for requirements with children.

    Args:
        req_id: The requirement ID of the requirement for which to search for children.
        other_req (dict): The definition for the requirement currently being checked against req_id.

    Returns:
        Optionally returns a dict containing any found child relationships.
    """
    return _get_requirement_ancestry(req_id, other_req, "children")


def _get_parent_requirements(req_id: str, other_req: dict) -> Optional[dict]:
    """
    Helper method that calls _get_requirement_ancestry() for requirements with parents.

    Args:
        req_id: The requirement ID of the requirement for which to search for parents.
        other_req (dict): The definition for the requirement currently being checked against req_id.

    Returns:
        Optionally returns a dict containing any found parent relationships.
    """
    return _get_requirement_ancestry(req_id, other_req, "parents")


def _get_requirement_ancestry(req_id: str, other_req: dict, direction: str) -> Optional[dict]:
    """
    Helper method that returns any present child-parent relationships between two requirements.

    Args:
        req_id: The requirement ID for which to search for hierarchy relationships.
        other_req (dict): The definition for the requirement currently being checked against req_id.

    Returns:
        Optionally returns a dict containing any found hierarchy relationships.
    """
    if direction in other_req.structure["req"]:
        if req_id in other_req.structure["req"][direction]:
            other_req_ids = other_req.structure["req"]["id"]
            if direction == "parents":
                dir = "parent"
                other_dir = "child"
            if direction == "children":
                dir = "child"
                other_dir = "parent"
            return {dir: req_id, other_dir: other_req_ids, "arrow": "+--", "relationship": ""}
