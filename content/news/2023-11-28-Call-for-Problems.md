---
title: Call for Problems that shall be addressed in the future development of the FMI standard
date: 2023-11-28
---

Currently the FMI project starts working on FMI 3.1 and would like the to ask the FMI user community to report their current pain points and ideas for future development. 

We currently have the idea to work on efficiency: we have identified that for FMUs that handle a large amount of data communication compared to internal calculations, the current design of FMI leads to overhead due to copy operation of data. 
This could be either due to a very large amount of scalar variables, or large data amounts in form of array or binary variables. 
Several solution approaches are in discussion, but currently the problem itself his not yet fully clear and has not yet been described in detail. 
So, if you face efficiency problems in the simulation of FMUs that can be traced back to communication overhead, please report them to us in form of use case description and problem statement.

More generally, if you have problems w.r.t. model exchange and co-simulation that cannot yet be solved well with FMI 3.0, please proivide them in the form of an Github issue (https://github.com/modelica/fmi-standard/issues) or via e-mail to contact@fmi-standard.org.
