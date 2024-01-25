# Rules of the Modelica Association Project (MAP) Functional Mock-up Interface (FMI)

Revisions:

2023/28/11 CB: Distinguish between Contributing Members and Advisory Board.

2016/05/31	AJ: Changed to reflect discussion and consensus during FMI Steering meeting 30.5.2016 a00nd email after that:

* Removed the addition to the BSD-2 license to make it more easily acceptable to large corporations and because current court cases indicate this addition not necessary
* Added Publication section that requires the FMI MAP to have MA confirm all standard publications.

2016/05/13	TB, AJ: Changes according to remarks from dSPACE and BOSCH.

* Bylaws to Rules changed, CCLA adapted
* Sentence with voting rights clarified, shortened, order changed.
* Inactivity removed and clarified.
* "Visitors do not have…" replaced by " Visitors have no right to access…". This allows to grant access for good reasons.
* "Contributor" replaced by "Organizations that contribute…"

2016/05/06	TB, AJ: Several additions:

* Definition of Organization added
* Rule for removal of inactive members added
* Publication of minutes restricted.

2015/06/19	AP: Clarification for license for project results

2015/06/02	TB: Several additions according to discussion in Steering Committee:

* Clarification of license of project results
* Introduction of a deputy project leader
* 66 % quorum for votes in the Steering Committee
* Clarification of openness of meetings
* Introduction of FMI Development Rules document
* Introduction of Corporate Contributor License Agreement (CCLA)
* Removal of list of initial members

2012/12/05	Slightly changed formatting. No voting needed for Advisory Committee members

2011/10/06	First version as part of the MAP application. Approved by the General Assembly meeting of the ITEA2 project Modelisar.

## Project purpose

Development, standardization and promoting the Functional Mockup Interface (FMI) definition.
The intention is that dynamic system models of different software systems can be used together for software/model/hardware-in-the-loop simulation and for embedded systems.

## License of project results

FMI specifications are published under the CC-BY-SA (Creative Common Attribution ShareAlike 4.0 International) license (or a follow-up version of this license), a human-readable summary of the license text as well as a link to the license text itself is available from https://creativecommons.org/licenses/by-sa/4.0/

Source code or other data, such as C-header and XML-schema files, that accompany the specification documents are provided under the BSD 2-Clause license (or a follow-up version of this license). A human-readable summary of the license text is available from http://www.opensource.org/licenses/bsd-license.html

## Project rules

The project rules are according to the rules of the Modelica Association Bylaws. In particular:

Project members::
Membership in this project is open to companies, institutes, universities and other organizations, which agree to support the purpose of this project and follow the project rules. 
There is no individual membership for this project. 
An organizational member has to appoint an individual person affiliated to the organization to represent the organization in all matters related to this project. 
This person is the organization’s liaison member. The liason member can nominate deputies with voting rights for individual meetings.

Project members are divided into three groups with a hierarchy of duties and rights: "Steering Committee Members" are a subset of "Contributing Members" which are a subset of
"Advisory Commitee Members":


Group 1: **Steering Committee**

1.	The members define FMI policy, strategy, feature roadmap, and future FMI Standard releases and other publications such as Layered standards.
2.	Members are organizations that actively support FMI. For the matter of clarity: A member need not to be a member of the Modelica Association.
3.	Members have voting rights (one vote for one organization, details see below).
4.	Members elect a project leader and a deputy project leader for 2 years with qualified majority (see below). 
The project leader must be an individual member of the Modelica Association, or must be the liaison member of an organizational member of the Modelica Association. 
Both have to be affiliated with an FMI Steering Committee member. 
The deputy supports the project leader and takes over the project leader's duties temporarily when the project leader is not available for a longer period.
5. The members decide on the release of new versions of the FMI Standard (published by MA, for major and minor release after confirmation by MA memebers) and the release of Layered Standards.
6.	The Steering Committee is open for additional members that proved to actively support FMI. Requirements:
* Must have participated at least at two FMI meetings (face to face or via electronic media) in the last 24 months, 
* must either provided the FMI standard or part of it in a commercial or open source tool, and/or must actively use FMI in industrial projects, 
* must have signed the Corporate Contributor License Agreement (CCLA, see below), (d) the members of the Steering Committee agree with qualified majority (see below).

Group 2: **Contributing Members**
1.	Consists of organizational members that have no voting rights and the FMI Steering Committee members.
2.	Contribute to the design of FMI by participation in working groups and by creating and editing Pull Request for the FMI standard on https://github.com/modelica/fmi-standard (and for layered standards).
3.	Have access to the internal infrastructure of the FMI design (Github repos, mailing lists, meeting minutes, etc.).
4.	The Group of Contributing Members is open for additional members that proved to actively support FMI. Requirement:
Must have signed the Corporate Contributor License Agreement or Modelica Assocation CLA. No voting is necessary for becoming a Contributing Member.


Group 3: **Advisory Committee**
1.	Consists of organizational members that have no voting right and the Steering Committee Members and Contributing Members.
2.	Contribute to the design of FMI by providing requirements and feedback. This can also be in the form of separate Advisory Board Meetings.
3.	Have access to the internal infrastructure of the FMI design (Github repos, mailing lists, meeting minutes, etc.).
4.	The Advisory Committee is open for additional members that proved to actively support FMI. 
Requirement:
Participation in at least two meetings as visitor. The FMI Steering Committee votes on acceptance to the Advisory Committee.


Project members that have not participated in meetings and have not contributed to the project for more than two years and did not react on a four weeks prior notice lose their membership after a vote with qualified majority. 
These organizations are excluded from the quorum for this decision.

*Visitors*
Organizations that contribute to the FMI Project and are neither in Group 1 or 2 are called “Visitors”. 
Visitors have no right to access to the internal infrastructure of the FMI project (svn, trac, mailing lists, etc.).

**Organizations**
An entity and all other entities that control, are controlled by, or are under common control with that entity are considered to be a single organization. 
For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

**Voting**
Voting is performed by the Steering Committee Members according to § 14 of the MA Bylaws but with a quorum of 66 % of the members. If explicitly decided by the Steering Committee Members, every voting can be performed electronically according to § 14 of the MA Bylaws.
New releases of the FMI specification and accompanying source code (like C-header or xml schema files) shall be approved by the Steering Committee Members with a qualified majority of the number of votes submitted. 

**Meetings**
FMI-meetings are announced in the respective mailing lists:

* Steering Committee meetings via steering@fmi-standard.org, the announcement must be at least 3 weeks in advance
* all other meetings via the other mailing lists (design@fmi-standard.org, and/or info@fmi-standard.org)

The Steering Committee decides whether a Steering Committee meeting is public or not, the default is private to ensure an efficient procedure. 
All other meetings are open to the public. 
The meeting material (minutes, documents, presentations) is available on the FMI-repository. A publication of this material needs approval of all participants.

**Development**
The development of FMI specifications is organized according to the FMI Development Rules (https://github.com/modelica/fmi-design/tree/master/FMI_DevelopmentProcess)
All organizations that contribute to an FMI specification and related works have to sign the Corporate Contributor License Agreement (https://svn.fmi-standard.org/fmi/branches/public/docs/CCLA) by a responsible representative of the company they are affiliated with.

**Publications**
The FMI Standard is published by the Modelica Association after confirmation by the MA members (vote with simple majority for major and minor releases). 
Other Publications such as bugfix releases of the FMI standard and Layered Standards can be published by the FMI project. 
