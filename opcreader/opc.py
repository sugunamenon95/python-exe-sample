"""Tools for reading metadata from OPC packages"""
import json
import sys
import xml.etree.cElementTree as ET
import zipfile


def get_content_types(fname):
    """Return content types as a dictionary.
    keys = part names
    values = content type for each part
    """
    tree = ET.fromstring(zipfile.ZipFile(fname).read("[Content_Types].xml"))

    content_types = dict()
    for elem in tree.iter():
        if "PartName" in elem.attrib and "ContentType" in elem.attrib:
            key = elem.attrib["PartName"]
            value = elem.attrib["ContentType"]
            content_types[key] = value

    return content_types

def get_relationships(fname):
    """Return package relationships as a dictionary.
    keys = Relationship Id
    values = Relationship Type
    """
    tree = ET.fromstring(zipfile.ZipFile(fname).read("_rels/.rels"))

    relationships = dict()
    for elem in tree.iter():
        if "Id" in elem.attrib and "Type" in elem.attrib:
            key = elem.attrib["Id"]
            value = elem.attrib["Type"]
            relationships[key] = value

    return relationships

