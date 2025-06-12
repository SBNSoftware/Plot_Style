# SBND plotting guidelines and recommendations

We are collecting comments and suggestions in [this googledoc](https://docs.google.com/document/d/1gxDuPT8zzrf3284mkZ_35KVOh_leFdQUiu6VjdEdUOw/edit?tab=t.0#heading=h.6osd0ywofj87).
Please share your thoughts! 

## Introduction

These guidelines apply to official plots.
[Requirements](#requirements) are mandatory unless there is a strong reason for not complying.
[Recommendations](#recommendations) are highly encouraged, but not mandatory.
See [SBNDStyle.h](https://github.com/SBNSoftware/Plot_Style/blob/main/SBNDStyle.h) for examples.

## Requirements
All plots **must**:

- **Be labelled with SBND official plot types**:     
  _SBND_, _SBND Preliminary_, or _SBND Work in Progress_.  
  See the [SBND publication policy](https://sbn-docdb.fnal.gov/cgi-bin/sso/ShowDocument?docid=1542).
- **Be easily readable**.
  See [recommendations](#recommendations) below for further advice.
- **Be saved in at least in one vector-based format** (e.g., pdf or eps, good for articles),
and **at least one high-quality raster-based format** (e.g., png, good for slides).

## Recommendations

### General advice

- Ensure all numbers shown have only a reasonable number of significant figures.   
- When applicable, add identifying information of the plot (e.g. Year, POT).

### Font and font size

- Use a sans serif font (e.g. Helvetica). Use consistent fonts across a single plot.
- Ensure plot text size is similar to that in the body of the article. Check the minimum text size guideline from the journal/conference organizers (typically 5 pt minimum).

### Color palette:

- Color palette should be accessible to those with color-vision deficiency (CVD). A CVD palette and a subset corresponding to SBND logo color (as close as we can - SBND logo is not really color-safe) can be found in [SBNDStyle.h](https://github.com/SBNSoftware/Plot_Style/blob/main/SBNDStyle.h).
- For continuous color ranges (e.g. z-axis of 2D histograms), use monochrome or [CVD-friendly color palettes](https://root.cern.ch/doc/master/classTColor.html#C06a).

### Axis labels & titles:

- Always include units in labels unless a quantity is unitless. Use parentheses for units: e.g., "Mass (GeV)".
- Titles should be centered along the axes.
- When histograms have variable binning or a bin width not divisible by the axis tick divisions, the "counts" axis should include the bin width: e.g., "Events / 10 MeV". 

### Lines and markers:

- **Data** should be indicated by black solid points with **error bars** unless there is a reason to do otherwise. 
- Models/simulation should be colored lines or step-histograms with (hatched) error bands.
- Refrain from connecting points/markers unless there’s a good reason to do so.
- When multiple lines or markers are shown, differentiate them using both color and line style (e.g., blue dashed line v.s. black solid line, red cross v.s. black square).
- Lines should be thick enough (2pt minimum) to be easily read from a distance. Markers should be larger than line width.

### Legends:

- Do not cover figure contents.
- Items should appear in the same top-to-bottom order as they are drawn in a histogram stack, if applicable.

### Special guidance for Event Displays

- Check [guidelines for making public event displays](https://sbn-docdb.fnal.gov/cgi-bin/sso/ShowDocument?docid=37119)

## References

- [Nature guideline](https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/)
- [Physical Review guideline](https://cdn.journals.aps.org/files/styleguide-pr.pdf)
