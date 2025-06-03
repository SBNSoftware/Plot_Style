# SBND plotting guidelines and recommendations

We are collecting comments and suggestions in [this googledoc](https://docs.google.com/document/d/1gxDuPT8zzrf3284mkZ_35KVOh_leFdQUiu6VjdEdUOw/edit?tab=t.0#heading=h.6osd0ywofj87).
Please share your thoughts! 

## Introduction

These guidelines apply to official plots.
[Requirements](#requirements) are mandatory unless there is a strong reason for not complying.
[Recommendations](#recommendations) are highly encouraged, but not mandatory.

## Requirements
All plots **must**:

- **Be labelled with the appropriate watermark**:     
  _SBND_, _SBND Preliminary_, or _SBND Work in Progress_.  
  See the [SBND publication policy](https://sbn-docdb.fnal.gov/cgi-bin/sso/ShowDocument?docid=1542).
- **Be easily readable**.
  See [recommendations](#recommendations) below for further advice on what this might mean in practice.
- **Be saved in at least in one vector-based format** (e.g., pdf or eps),  
  and **at least one high-quality raster-based format** (e.g., png).

## Recommendations

### General advice

- Ensure all numbers shown have only a reasonable number of significant figures.   
- Where appropriate, add explicit identifying information of the plot (eg Year, POT).
- Differentiate datasets using both color and line style (e.g., dashed vs solid).

### Font and font size

- Use a sans serif font. Use consistent fonts across a single plot.
- Ensure plot text size is similar to that in the body of the article as possible. Check the minimum text size guideline from the journal/conference organizers.

### Colo(u)r palette:
All below options are supported in SBNDStyle.h:

- Color choices should look appealing and be accessible to those with color-vision deficiency (CVD), such as the [Okabe-Ito color cycle](https://jfly.uni-koeln.de/color/) colors. 
- A subset corresponding to SBND logo color (as close as we can - SBND logo is not really color-safe) can be accessed in Cycle::SBNDLogo)
- For continuous color ranges (e.g. z-axis of 2D histograms), use monochrome, bichrome, or the [cividis color palette](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0199239).

### Axis labels & titles:

- Use consistent capitalization. 
- Always include units in labels unless a quantity is unitless. Use parentheses for units: e.g., "Mass (GeV)".
- Titles should be centered along the axes.
- When histograms have variable binning or a bin width not divisible by the axis tick divisions, the "counts" axis
  (y (z)-axis for a 1 (2)-D histogram) should include the bin width: e.g., "Events / 10 MeV". 

### Lines and markers:

- Data should generally be indicated by black solid points with error bars unless there is a reason to do otherwise.
- Refrain from connecting points/markers unless there’s a good reason to do so.
- Models/simulation should be lines or step-histograms to differentiate from data (unless statistical uncertainty of MC sample is significant).
- When multiple lines or markers are shown, use distinct line or marker styles to distinguish them in addition to color choices. This aids in accessibility. 
- Lines should be thick enough (2pt or thicker) to be easily read from a distance.
- Consider whether using separate statistical and systematic error bars make sense in the context of your plot.
- Prefer using error bands for simulation and error bars for data.

### Legends:

- Do not cover figure contents.
- Items should appear in the same top-to-bottom order as they are drawn in a histogram stack, if applicable.

### Special guidance for Event Displays
- Add data/simulation labels. If data, add Run/Subrun/Event and date text overlaying event display.
- Overlay SBND logo.
