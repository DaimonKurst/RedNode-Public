"""
RedNode Public Demo Module

Synthetic runtime chain builder.
This is a documentation-oriented example and does not execute attacks.
"""


def build_runtime_chain():
    return {
        "mode": "SAFE_READ_ONLY",
        "nodes": [
            "TARGET_INIT",
            "HAR_ANALYSIS",
            "ENDPOINT_EXTRACTION",
            "ATTACK_SURFACE_MAPPING",
            "HUMAN_REVIEW",
        ],
        "edges": [
            ("TARGET_INIT", "HAR_ANALYSIS"),
            ("HAR_ANALYSIS", "ENDPOINT_EXTRACTION"),
            ("ENDPOINT_EXTRACTION", "ATTACK_SURFACE_MAPPING"),
            ("ATTACK_SURFACE_MAPPING", "HUMAN_REVIEW"),
        ],
    }


if __name__ == "__main__":
    print(build_runtime_chain())
