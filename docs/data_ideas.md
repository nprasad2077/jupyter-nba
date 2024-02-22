# Data Viz Ideas

- Scoring Breakdown: Stacked bar charts showing the proportion of a player's points from field goals, three-pointers, and free throws for each season.
- Advanced Stat Progression: Plotly's ability to have multiple y-axes allows you to visualize stats like PER or Win Shares alongside traditional stats, providing a more nuanced picture of performance over time.

- Player Radar Charts: Use Plotly's radar charts to compare multiple advanced stats of players within the same season. This helps visualize a player's well-roundedness (e.g., scoring, rebounding, playmaking).
- Usage vs. Efficiency: Scatter plots showing usage percentage vs. true shooting percentage. Are high-usage players on a team also efficient scorers?
---

- "Constellation" Visuals: Imagine each advanced stat as a point on a circular graph. A player's profile is then a shape formed by connecting their values. This allows comparison of players with distinct styles (defensive specialist vs. high volume scorer).
- Franchise Value Over Time: Animated line graph where the line thickness represents 'total win shares' contributed by players currently on a team. This visualizes how "star power" has accumulated or faded.
- Interactive Player Analysis: A Dash app where users select a player, get their basic stats, and then choose from a dropdown for advanced visualizations (shot chart, efficiency over time, etc.).
---
- Position vs Stats: Create a bar chart that compares the average statistics (like points, assists, rebounds, etc.) for each position (PG, SG, SF, PF, C). This can provide insights into how the roles and responsibilities differ by position.
- Efficiency Metrics: Use field_goal percentages (FG%, 3P%, 2P%, FT%) or advanced stats (PER, TS%, Win Shares, VORP) to create a histogram or density plot showing the distribution of these measures. Highlight the performance of some notable players on these plots for context.
- Team Aggregates: Create a stacked bar chart or a pie chart to show total team statistics (like total points, total rebounds, total assists) for each team in a given season.
- Correlation Matrix: You can represent how each stat correlates to each other (PPP, PER, win shares, etc) in a correlation matrix heatmap.
- Player Comparison: Allow selecting two players, then provide head-to-head comparison with bar charts or radar/spider charts for different stats.
- Game Impact Over Minutes: Generate a scatter plot of Player Efficiency Rating (PER) versus minutes per game to evaluate how players' performance scales with their playtime.
- Win Shares Evolution: Win shares might be plotted over time (season) for a select set of 'star players', to visualize their contribution to team victories over their career.