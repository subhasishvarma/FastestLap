
import fastf1
import os

def get_fastest_laps(year, gp, session):
    cache_path = "cache"

    # Fix cache folder issues
    if os.path.exists(cache_path) and not os.path.isdir(cache_path):
        os.remove(cache_path)
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)

    fastf1.Cache.enable_cache(cache_path)

    # Load session
    ses = fastf1.get_session(year, gp, session)

    try:
        ses.load()
    except Exception as e:
        raise RuntimeError(f"Session data could not be loaded: {e}")

    # Process fastest laps
    laps = ses.laps.pick_quicklaps()
    if laps.empty:
        raise RuntimeError("No lap data found for this session.")

    fastest = laps.groupby('Driver').apply(lambda x: x.pick_fastest()).reset_index(drop=True)
    fastest['LapTimeSeconds'] = fastest['LapTime'].dt.total_seconds()

    return fastest
