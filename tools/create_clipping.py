#!/usr/bin/env python3
"""
Create a macOS .textClipping file suitable for Indigo Control Page import.

Part of the indigo-control-pages skill for Claude Code.
https://github.com/simons-plugins/indigo-control-pages

A .textClipping file is a binary plist with two top-level keys:
  - 'UTI-Data': dict containing the text in multiple encodings
  - 'OSType-Data': dict containing NSKeyedArchiver metadata

The UTI-Data dict has three keys:
  - 'public.utf8-plain-text': str - the text as a Python string
  - 'public.utf16-plain-text': bytes - the text encoded as UTF-16LE (no BOM)
  - 'com.apple.traditional-mac-plain-text': bytes - the text encoded as Mac Roman (CR line endings)

Usage:
    python3 create_clipping.py <output_path> [--name <display_name>]

    Reads XML from stdin or pass --xml <string>.

Examples:
    echo '<ControlPageList>...</ControlPageList>' | python3 create_clipping.py ~/Desktop/MyPage.textClipping
    python3 create_clipping.py output.textClipping --xml '<ControlPageList type="vector">...</ControlPageList>'
"""

import plistlib
import sys
import argparse


def build_ostype_data(item_names: list[str]) -> bytes:
    """
    Build the NSKeyedArchiver binary plist that goes into OSType-Data[''].

    This encodes an NSDictionary with key 'ItemArray' pointing to an
    NSMutableArray of item name strings. This mirrors what macOS Finder
    creates when making a .textClipping.

    Args:
        item_names: list of item name strings (e.g., page names from the XML)

    Returns:
        Binary plist bytes (NSKeyedArchiver format)
    """
    objects = [
        "$null",  # 0
    ]

    # Index 1: root NSDictionary
    root_dict_idx = 1
    objects.append(None)  # placeholder

    # Index 2: "ItemArray" key
    item_array_key_idx = 2
    objects.append("ItemArray")

    # Index 3: NSMutableArray
    array_idx = 3
    objects.append(None)  # placeholder

    # Indices 4+: item name strings
    name_start_idx = 4
    for name in item_names:
        objects.append(name)

    # NSMutableArray class definition
    mutable_array_class_idx = name_start_idx + len(item_names)
    objects.append({
        "$classname": "NSMutableArray",
        "$classes": ["NSMutableArray", "NSArray", "NSObject"],
    })

    # NSDictionary class definition
    dict_class_idx = mutable_array_class_idx + 1
    objects.append({
        "$classname": "NSDictionary",
        "$classes": ["NSDictionary", "NSObject"],
    })

    # Fill in the NSMutableArray (index 3)
    name_uids = [plistlib.UID(name_start_idx + i) for i in range(len(item_names))]
    objects[array_idx] = {
        "NS.objects": name_uids,
        "$class": plistlib.UID(mutable_array_class_idx),
    }

    # Fill in the root NSDictionary (index 1)
    objects[root_dict_idx] = {
        "NS.keys": [plistlib.UID(item_array_key_idx)],
        "NS.objects": [plistlib.UID(array_idx)],
        "$class": plistlib.UID(dict_class_idx),
    }

    archiver_plist = {
        "$version": 100000,
        "$archiver": "NSKeyedArchiver",
        "$top": {"root": plistlib.UID(root_dict_idx)},
        "$objects": objects,
    }

    return plistlib.dumps(archiver_plist, fmt=plistlib.FMT_BINARY)


def create_text_clipping(xml_text: str, output_path: str, item_names: list[str] | None = None):
    """
    Create a macOS .textClipping file from an XML string.

    Args:
        xml_text: The Indigo XML content to store in the clipping
        output_path: Path to write the .textClipping file
        item_names: Optional list of item names for OSType-Data metadata.
                    If None, extracts <Name> elements from XML or uses ["Item"].
    """
    if item_names is None:
        import re
        names = re.findall(r'<Name type="string">([^<]+)</Name>', xml_text)
        item_names = names if names else ["Item"]

    # Build the three text representations
    utf8_text = xml_text
    utf16_bytes = xml_text.replace("\n", "\r").encode("utf-16-le")
    mac_text = xml_text.replace("\n", "\r").encode("mac-roman", errors="replace")

    # Build the OSType-Data (NSKeyedArchiver with ItemArray)
    ostype_bytes = build_ostype_data(item_names)

    # Assemble the top-level plist
    clipping = {
        "OSType-Data": {
            "": ostype_bytes,
        },
        "UTI-Data": {
            "com.apple.traditional-mac-plain-text": mac_text,
            "public.utf16-plain-text": utf16_bytes,
            "public.utf8-plain-text": utf8_text,
        },
    }

    # Write as binary plist
    with open(output_path, "wb") as f:
        plistlib.dump(clipping, f, fmt=plistlib.FMT_BINARY)

    import os
    file_size = os.path.getsize(output_path)
    print(f"Created: {output_path}")
    print(f"  XML length: {len(xml_text)} chars")
    print(f"  Item names: {item_names}")
    print(f"  File size: {file_size} bytes")


def main():
    parser = argparse.ArgumentParser(
        description="Create a macOS .textClipping file from Indigo Control Page XML"
    )
    parser.add_argument("output", help="Output .textClipping file path")
    parser.add_argument("--xml", help="XML string (if not provided, reads from stdin)")
    parser.add_argument(
        "--name",
        action="append",
        dest="names",
        help="Item name(s) for metadata (can be repeated; auto-detected from XML if omitted)",
    )
    args = parser.parse_args()

    if args.xml:
        xml_text = args.xml
    else:
        xml_text = sys.stdin.read()

    if not xml_text.strip():
        print("Error: No XML input provided", file=sys.stderr)
        sys.exit(1)

    create_text_clipping(xml_text, args.output, item_names=args.names)


if __name__ == "__main__":
    main()
