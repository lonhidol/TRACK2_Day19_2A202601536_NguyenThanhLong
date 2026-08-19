import sys
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

# Add project root to path
sys.path.append("/Users/ryu/Documents/pythonweb/AITHUCCHIEN/TRACK2_Day19_2A202601536_NguyenThanhLong")

import pandas as pd
from feast import FeatureStore

NOW = datetime.now(timezone.utc).replace(microsecond=0)
FEAST_DIR = "/Users/ryu/Documents/pythonweb/AITHUCCHIEN/TRACK2_Day19_2A202601536_NguyenThanhLong/app/feast_repo"

fs = FeatureStore(repo_path=FEAST_DIR)
entity_df = pd.DataFrame({
    "user_id": ["u_001", "u_002", "u_003"],
    "event_timestamp": [NOW - timedelta(hours=2), NOW - timedelta(hours=1), NOW],
})

historical = fs.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_profile_features:reading_speed_wpm",
        "user_profile_features:topic_affinity",
    ],
).to_df()
print(historical)
