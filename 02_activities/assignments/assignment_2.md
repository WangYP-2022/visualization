# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Good visualization.
https://public.tableau.com/app/profile/gurpreet.singh2669/viz/BeatRot-VizforsustainabilityChallenge2024/Impact. This food waste sustainability dashboard exemplifies effective data visualization principles through its clear hierarchical structure and logical information flow. Following best practices from our course material on subplot layouts (Slide deck 06), the visualization uses a well-organized mosaic arrangement that guides viewers from high-level statistics (top banner) through geographic patterns (map) to detailed breakdowns (bar charts). This progressive disclosure helps viewers build understanding systematically rather than overwhelming them with simultaneous information.
The color scheme demonstrates sophisticated design choices. The visualization employs a consistent earth-tone palette (browns, oranges, greens) that reinforces the sustainability theme while maintaining excellent contrast for readability. As covered in Slide deck 05 regarding color usage and styling, the limited color palette (approximately 4-5 colors) prevents visual confusion while using color meaningfully – green for positive impact, orange/brown for waste metrics. The choropleth map uses appropriate sequential shading that clearly communicates data intensity without distortion.
Chart type selection is highly appropriate for each data story. The combination of KPI cards, geographic visualization, and bar charts follows Cairo's principle of matching visual form to data type. The horizontal bar charts effectively compare categorical data (food types and disposal methods), making relative magnitudes immediately apparent. The map visualization appropriately shows geographic distribution without misleading projections or inappropriate 3D effects that Tufte warns against.
Labeling and annotation excellence distinguishes this visualization. Every chart includes clear titles, axis labels, and data labels where appropriate. The top banner prominently displays key metrics with context ("Total Food Wasted: 931M tonnes" with percentage breakdowns), following annotation principles from Slide deck 05. The subtitle "Understanding the environmental footprint of food waste" immediately communicates purpose, addressing the common failure of visualizations lacking context.
Accessibility and clarity are evident throughout. The visualization avoids common pitfalls like truncated axes, misleading scales, or chartjunk. Text is legible, hierarchies are clear through font sizing (Slide deck 05 fontdict principles), and white space is used effectively to separate distinct analytical sections. The layout could work in both interactive and static formats, demonstrating good design fundamentals.

      
      Bad visualization. 
https://public.tableau.com/app/profile/nastengraph/viz/BoringMonacoF1DriversStart-FinishPositionsinMonacoGP/BoringMonaco. This Monaco Grand Prix visualization fails on multiple fundamental design principles covered in our course material. The primary issue is visual clutter and cognitive overload – the chart attempts to display every driver's start-to-finish position across multiple years using intersecting lines, creating what Edward Tufte calls "chartjunk." The dense overlapping lines make it nearly impossible to trace individual driver performances, defeating the visualization's core purpose.
The color scheme is problematic: with numerous drivers represented simultaneously, the visualization uses too many similar colors without sufficient contrast, violating accessibility principles. As discussed in Slide deck 05 regarding effective color usage, distinguishing between adjacent lines becomes extremely difficult, particularly for colorblind users. The lack of a clear legend or color-coding system further compounds this issue.
Inappropriate chart type selection represents another critical flaw. While slope charts work well for comparing two points, this visualization attempts to show trajectories across multiple races, creating a "spaghetti chart" that obscures patterns rather than revealing them. According to data visualization best practices (Cairo, 2016), chart selection should prioritize clarity over complexity – this visualization does the opposite.
The labeling system is insufficient. Individual lines lack clear markers or labels, requiring viewers to hover over each line to identify drivers. This interactive dependency makes the visualization unusable in printed or static formats. Course material on annotations (Slide deck 05) emphasizes that critical information should be immediately visible without requiring user interaction.
Finally, the visualization suffers from missing context and explanation. There's no clear title explaining what "boring" means quantitatively, no axis labels explaining the position scale, and no temporal indicators showing which years are included. The subtitle "Start-Finish Positions" is vague – does it show improvement, consistency, or overtaking frequency?


      ```
    - How could this data visualization have been improved?  
      ```
      Good visualization.

While this is a strong visualization, minor refinements could enhance clarity further. The map could benefit from error bars or confidence intervals (Slide deck 06) showing data quality variation across countries, particularly where reporting standards differ. Adding small indicators of statistical uncertainty would increase credibility without cluttering the design.
Interactive enhancements could improve engagement: implementing tooltips showing additional context (e.g., hovering over countries reveals per-capita waste or trend data), adding year filters to show temporal changes, or enabling drill-down functionality from the map to country-specific breakdowns. These additions would leverage the digital medium while maintaining the clean static design.
Annotation improvements could highlight key insights more prominently. Following Slide deck 05's annotation techniques, adding strategic text boxes with arrows could draw attention to surprising findings (e.g., "Household waste accounts for 61% of total" with an arrow to the relevant bar). Currently, viewers must discover patterns themselves; guided annotations would accelerate comprehension.
Additional context through legends would help. While the color scheme is intuitive, adding a small legend explaining the map's color gradation (e.g., "tonnes of food waste: light = <10M, dark = >50M") and including data sources with dates would increase transparency and credibility. The visualization could also benefit from a brief methodology note explaining how waste was measured.
Comparative elements could strengthen the analysis. Adding a small reference line or secondary axis showing "target reduction goals" on the bar charts would provide benchmarks for evaluating current performance. Similarly, a small inset showing year-over-year trends would add temporal context to these static snapshots, helping viewers understand whether the situation is improving or worsening.
      
      Bad visualization. 
Simplification is essential. Rather than showing all drivers simultaneously, implement filtering or faceting (as demonstrated in subplot_mosaic from Slide deck 06). Create separate small multiples for each team or season, allowing meaningful comparison without visual chaos. Alternatively, focus on top performers or specific storylines (e.g., "drivers who started outside top 10 but finished on podium").
Redesign the chart type: Replace the slope chart with a scatter plot with error bars (Slide deck 06) showing average starting position versus average finishing position, with error bars indicating consistency. This would immediately reveal which drivers typically improve or maintain positions. Alternatively, use a heatmap showing position changes by driver and year, providing clear patterns without line overlap.
Improve color and legend implementation: Limit the visualization to 5-7 drivers maximum, using high-contrast colors from established palettes (as covered in styling, Slide deck 05). Add a clear legend with driver names and team affiliations. For comprehensive data, implement interactive filters allowing users to select specific drivers or years.
Enhance labeling and annotations: Add clear axis labels ("Starting Grid Position" and "Finishing Position"), include year markers on the x-axis, and annotate notable performances (e.g., "Hamilton: +10 positions, 2008"). Following Slide deck 05's annotation principles, highlight exceptional cases with text boxes and arrows pointing to specific data points.
Provide context: Add a descriptive title like "Monaco GP Overtaking Analysis: Driver Start vs. Finish Positions (2010-2023)" and include summary statistics showing that Monaco typically has fewer position changes than other circuits, justifying the "boring" descriptor with actual data.


      
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 10/26/2025`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
