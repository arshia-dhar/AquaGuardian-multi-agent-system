import pandas as pd
from security.validation import validate_file

def analyze_telemetry(csv_path: str) -> str:
    validate_file(csv_path)
    """
    Analyze AUV mission telemetry from a CSV file.

    Expected columns:
    - time
    - depth
    - battery
    - x
    - y

    Args:
        csv_path: Path to the telemetry CSV file.

    Returns:
        A human-readable summary of mission performance.
    """

    try:
        # Load telemetry data
        df = pd.read_csv(csv_path)

        if df.empty:
            return "The telemetry file is empty."

        summary = []

        # Mission duration
        if "time" in df.columns:
            duration = df["time"].iloc[-1] - df["time"].iloc[0]
            summary.append(
                f"Mission duration: {duration:.2f} time units."
            )
        else:
            summary.append(
                f"Mission contains {len(df)} recorded samples."
            )

        # Battery analysis
        if "battery" in df.columns:
            start_battery = df["battery"].iloc[0]
            end_battery = df["battery"].iloc[-1]
            consumed = start_battery - end_battery

            summary.append(
                f"Battery consumed: {consumed:.2f}% "
                f"(from {start_battery:.1f}% to {end_battery:.1f}%)."
            )

            if end_battery < 20:
                summary.append(
                    "⚠ Warning: Battery level dropped below 20%."
                )

        # Depth analysis
        if "depth" in df.columns:
            max_depth = df["depth"].max()
            min_depth = df["depth"].min()
            avg_depth = df["depth"].mean()

            summary.append(
                f"Depth profile: min={min_depth:.2f} m, "
                f"max={max_depth:.2f} m, "
                f"average={avg_depth:.2f} m."
            )

            if df["depth"].std() > 5:
                summary.append(
                    "⚠ Significant depth fluctuations detected."
                )
            else:
                summary.append(
                    "No major depth anomalies detected."
                )

        # Navigation analysis
        if {"x", "y"}.issubset(df.columns):
            distance = (
                ((df["x"].diff()) ** 2 +
                 (df["y"].diff()) ** 2) ** 0.5
            ).sum()

            summary.append(
                f"Estimated distance travelled: {distance:.2f} units."
            )

        # Overall mission assessment
        summary.append(
            "Mission telemetry analysis completed successfully."
        )

        return "\n".join(summary)

    except FileNotFoundError:
        return f"Telemetry file not found: {csv_path}"

    except pd.errors.EmptyDataError:
        return "The telemetry file contains no data."

    except Exception as e:
        return f"Error analyzing telemetry: {str(e)}"