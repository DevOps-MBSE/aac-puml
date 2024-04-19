from typing import List, Optional

def _get_requirements_defs(reqs: dict) -> List[dict]:

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
            connected = _get_connected_requirements(req, reqs, [])
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
    if not attributes:
        attributes = [{}]
    for attribute in attributes:
        if attribute["name"] == "type":
            return attribute["value"]

def _get_connected_requirements(req: dict, reqs: dict, connected_reqs: List[dict]) -> List[dict]:
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

def _get_child_requirements(req_id: str, other_req: dict):
    return _get_requirement_ancestry(req_id, other_req, "children")

def _get_parent_requirements(req_id:str, other_req: dict):
    return _get_requirement_ancestry(req_id, other_req, "children")

def _get_requirement_ancestry(req_id: str, other_req: dict, direction: str) -> Optional[dict]:
    print(other_req)
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






