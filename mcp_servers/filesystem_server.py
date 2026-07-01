from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("AquaGuardianFilesystem")


MISSIONS_DIR = Path("missions")


@mcp.tool()
def list_missions() -> list[str]:
    """
    List all available mission folders.
    """

    if not MISSIONS_DIR.exists():
        return []

    return [
        p.name
        for p in MISSIONS_DIR.iterdir()
        if p.is_dir()
    ]


@mcp.tool()
def get_mission_files(mission_name: str) -> list[str]:
    """
    Return all files belonging to a mission.
    """

    mission_path = MISSIONS_DIR / mission_name

    if not mission_path.exists():
        return []

    return [
        str(file)
        for file in mission_path.iterdir()
        if file.is_file()
    ]


@mcp.tool()
def get_latest_mission() -> str:
    """
    Return the latest mission folder.
    """

    missions = sorted(
        MISSIONS_DIR.iterdir(),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    if not missions:
        return "No missions found."

    return missions[0].name


if __name__ == "__main__":
    mcp.run()