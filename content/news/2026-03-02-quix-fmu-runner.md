--
title: Quix FMU Runner added to the FMI Tools listing
date: 2026-03-02
---

Quix has released an open-source FMU Runner that executes FMI-compliant simulation models inside Docker containers and connects them to live data streams through [Quix Streams](https://github.com/quixio/quix-streams).

The runner supports FMI 2.0 and 3.0 Co-Simulation FMUs. It uses [FMPy](https://github.com/CATIA-Systems/FMPy) to load and simulate models, and publishes simulation configuration, as well as input and output data. This allows FMU models to participate in: 
- cross-tool engineering workflows (for example Simulink-to-Modelica integration)
- digital twin systems (where a model is excited by live data from a real device)
- virtual test benches (where a model is excited from historic data recorded by virtual or physical tests)

Whilst - all the while - data is consolidated to a single source of truth data warehouse for downstream analytics.

The project is designed to run on [Quix Cloud](https://quix.io/) but can also be deployed independently with open source technologies including Docker and Kafka.

Source code, documentation, and examples are available on GitHub: [quixio/template-fmu-runner](https://github.com/quixio/template-fmu-runner).