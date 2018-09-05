---
title: FMI 3.0-alpha feature list released
categories: [news]
layout: post
---

The FMI Steering Committee is happy to announce the preliminary (alpha) feature list for FMI 3.0.
_Preliminary_ means that we might be forced to drop some features from that list for the actual release.
This list is based on the results of the respective working groups which were discussed at the FMI Design Meeting Nov 2017.

- **Ports and Icons**: Help the user to build consistent systems from FMUs and render the systems more intuitively with better representation of structured ports (for instance busses and physical connectors) in the modelDescription.xml.

- **Array variables**: Allow FMUs to communicate multi-dimensional variables and change their sizes using structural parameters.

- **Clocks and Hybrid Co-Simulation**: Introduces clocks for synchronization of variables changes across FMUs. Allows co-simulation with events.

- **Binary Data Type**: Adds an opaque binary data type to FMU variables to allow, for instance, efficiently exchanging of complex sensor data.

- **Intermediate Output Values**: Allow access of intermediate output values between communication time points from the FMU to disclose relevant subsystem behavior for analysis or advanced co-simulation master algorithms.

- **Source code FMUs**: Adding more information to the modelDescription.xml file to improve automatic import of source code FMUs.

In the unlikely event of unsolvable conflicts between features, the FMI Steering Committee might be forced to again remove or alter features during the merge-phase of all FCPs starting after the release of the Beta feature list.
The FMI Steering Committee will make these FCPs available to interested parties on request once their maturity allows dissemination.
