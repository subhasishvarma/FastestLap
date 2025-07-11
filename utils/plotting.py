import matplotlib.pyplot as plt


def plot_fastest_laps(fastest_laps):
    fastest_laps['LapTimeSeconds'] = fastest_laps['LapTime'].dt.total_seconds()
    fastest_laps = fastest_laps.sort_values(by='LapTimeSeconds').reset_index(drop=True)

    team_color_map = {
        'Red Bull': 'royalblue',
        'Mercedes': 'silver',
        'McLaren': 'darkorange',
        'Ferrari': 'red',
        'Aston Martin': 'green',
        'RB': 'deepskyblue',
        'Alpine': 'darkblue',
        'Williams': 'lightblue',
        'Kick Sauber': 'black',
        'Haas F1 Team': 'gray',
    }

    y_values = fastest_laps['Driver']
    x_values = fastest_laps['LapTimeSeconds'].descending()
    bar_color = '#e0e0e0'

    def format_laptime(seconds):
        minutes = int(seconds) // 60
        sec = seconds % 60
        return f"{minutes}:{sec:05.2f}"

    fig, ax = plt.subplots(figsize=(10, 8))
    bars = ax.barh(y_values, x_values, color=bar_color)

    for i, bar in enumerate(bars):
        width = bar.get_width()
        team = fastest_laps.loc[i, 'Team']
        lap_label = format_laptime(width)
        team_color = team_color_map.get(team, 'dimgray')

        ax.text(width + 0.2,
                bar.get_y() + bar.get_height() / 2,
                lap_label,
                va='center', ha='left', fontsize=9)

        ax.text(bar.get_x() + 0.3,
                bar.get_y() + bar.get_height() / 2,
                team,
                va='center', ha='left',
                fontsize=8, fontweight='bold', color=team_color)

    ax.set_title("Fastest Lap Times by Driver", fontsize=14)
    ax.set_xlabel("Lap Time")
    ax.set_ylabel("Driver")
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    return fig
