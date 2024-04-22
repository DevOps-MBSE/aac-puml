from typing import List, Optional


def _get_requirements_defs(reqs: dict) -> List[dict]:
    """
    Helper method for extracting and sorting data from a requirement specification

    Args:
        reqs (dict): A dictionary of requirement definitions

    Returns:
        A List of dictionaries of organized data for diagram generation
    """
    requirements = []
    if reqs:
        for req_key in reqs:
            req = reqs[req_key]
            id = req.structure["req"]["id"]
            attributes = req.structure["req"]["attributes"]
            type = _get_requirement_type(attributes)
            title = None
            name = req.structure["req"]["name"]
            shall = req.structure["req"]["shall"]
            connected = _get_connected_requirements(req, reqs)
            requirements.append({
                "type": type,
                "title": title,
                "name": name,
                "id": id,
                "shall": shall,
                "attributes": attributes,
                "connected": connected,
            })
    return requirements


def _get_requirement_type(attributes: List[dict]) -> str:
    """
    Helper method for extracting the TADI type of a requirement

    Args:
        attributes (List[dict]): A List of a requirement definitions attributes

    Returns:
        The value of the TADI attribute
    """
    if not attributes:
        attributes = [{}]
    for attribute in attributes:
        if attribute["name"] == "TADI":
            print(attribute["value"])
            return attribute["value"]


def _get_connected_requirements(req: dict, reqs: dict) -> List[dict]:
    """
    Helper method that finds the parent and child requirement definitions for a specified requirement

    Args:
        req (dict): A requirement defintion
        reqs (dict): A dictionary containing all requirement definitions

    Returns:
        A list of parent and child requirement definitions for the specified requirement
    """
    connected_reqs = []
    if not reqs:
        return connected_reqs

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
    Helper method that calls _get_requirement_ancestry() for requirements with children

    Args:
        req_id: The requirement ID of the requirement for which we are searching for children
        other_req (dict): The definition for the requirement currently being checked against req_id

    Returns:
        Optionally returns a dict containing any found child relationships
    """
    return _get_requirement_ancestry(req_id, other_req, "children")


def _get_parent_requirements(req_id: str, other_req: dict) -> Optional[dict]:
    """
    Helper method that calls _get_requirement_ancestry() for requirements with parents

    Args:
        req_id: The requirement ID of the requirement for which we are searching for parents
        other_req (dict): The definition for the requirement currently being checked against req_id

    Returns:
        Optionally returns a dict containing any found parent relationships
    """
    return _get_requirement_ancestry(req_id, other_req, "children")


def _get_requirement_ancestry(req_id: str, other_req: dict, direction: str) -> Optional[dict]:
    """
    Helper method that returns any present child-parent relationships between two requirements

    Args:
        req_id: The requirement ID of the requirement for which we are searching for hierarchy relationships for
        other_req (dict): The definition for the requirement currently being checked against req_id

    Returns:
        Optionally returns a dict containing any found hierarchy relationships
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
