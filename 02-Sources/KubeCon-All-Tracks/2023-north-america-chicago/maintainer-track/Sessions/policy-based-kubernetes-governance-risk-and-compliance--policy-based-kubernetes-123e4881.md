---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Jim Bugwadia", "Nirmata", "Andy Suderman", "Fairwinds", "Poonam Lamba", "Google", "Anca Sailer", "IBM", "Robert Ficcaglia", "SunStone Secure"]
sched_url: https://kccncna2023.sched.com/event/1R2nk/policy-based-kubernetes-governance-risk-and-compliance-jim-bugwadia-nirmata-andy-suderman-fairwinds-poonam-lamba-google-anca-sailer-ibm-robert-ficcaglia-sunstone-secure
youtube_search_url: https://www.youtube.com/results?search_query=Policy-Based+Kubernetes+Governance%2C+Risk%2C+and+Compliance+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Policy-Based Kubernetes Governance, Risk, and Compliance - Jim Bugwadia, Nirmata; Andy Suderman, Fairwinds; Poonam Lamba, Google; Anca Sailer, IBM; Robert Ficcaglia, SunStone Secure

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Jim Bugwadia, Nirmata, Andy Suderman, Fairwinds, Poonam Lamba, Google, Anca Sailer, IBM, Robert Ficcaglia, SunStone Secure
- Schedule: https://kccncna2023.sched.com/event/1R2nk/policy-based-kubernetes-governance-risk-and-compliance-jim-bugwadia-nirmata-andy-suderman-fairwinds-poonam-lamba-google-anca-sailer-ibm-robert-ficcaglia-sunstone-secure
- Busca YouTube: https://www.youtube.com/results?search_query=Policy-Based+Kubernetes+Governance%2C+Risk%2C+and+Compliance+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Policy-Based Kubernetes Governance, Risk, and Compliance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2nk/policy-based-kubernetes-governance-risk-and-compliance-jim-bugwadia-nirmata-andy-suderman-fairwinds-poonam-lamba-google-anca-sailer-ibm-robert-ficcaglia-sunstone-secure
- YouTube search: https://www.youtube.com/results?search_query=Policy-Based+Kubernetes+Governance%2C+Risk%2C+and+Compliance+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=irFvAZ0IjSg
- YouTube title: Policy-Based Kubernetes Governance, Risk, and Compliance
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/policy-based-kubernetes-governance-risk-and-compliance/irFvAZ0IjSg.txt
- Transcript chars: 29728
- Keywords: policy, policies, compliance, platform, governance, practices, cluster, security, organization, everyone, within, environment, anyone, language, configuration, approach, controls, framework

### Resumo baseado na transcript

okay well as a homage to the Chicago musical is everybody here is everybody ready let's do it so welcome to the policy based governance risk compliance panel discussion uh we are the cncf kuini policy work group before I uh jump into the panel contents I'd like to introduce the panel we have Ana Siler distinguished engineer from IBM we have Andy sudman CTO of fnds Jim badia founder and CEO of nada and Punam Lama product manager at Google myself Robert vialia CTO of Sunstone secure uh I

### Excerpt da transcript

okay well as a homage to the Chicago musical is everybody here is everybody ready let's do it so welcome to the policy based governance risk compliance panel discussion uh we are the cncf kuini policy work group before I uh jump into the panel contents I'd like to introduce the panel we have Ana Siler distinguished engineer from IBM we have Andy sudman CTO of fnds Jim badia founder and CEO of nada and Punam Lama product manager at Google myself Robert vialia CTO of Sunstone secure uh I just a brief set of uh intro uh notes about the policy workg group our entire focus is to work with the Kuan community and discuss how policy can be made practical how it can be made better uh discuss architecture and best practices and so we we give a big welcome to everyone who is either working within the kubernetes project the constellation of other CNC projects or just in general as an operator or user of KUB entities to join if you have any interest or any contribution in the policy landscape or if not just to observe uh the work group has uh so far produced a number of outputs we have done some white papers on kuber unties policy management uh kind of a high level overview uh we have uh contributed back an API crd for policy output so there's a myriad different policy engines and ways to express those policies in different dsls we decided several years back that there was a need to at least to find some layer of abstraction that reporting can be done in a consistent way and so we've worked with a number of the projects and different Community contributions to have either native integration or or uh component Bridges adapters to that standard uh and then we just released our way paper on kubernetes governance risk compliance and that will be the focus of today uh we wanted to just get a quick show of hands on a couple of questions just to see where the familiarity is so uh for those who are implementing or planning to implement a kubernetes environment um let's say are you aware of using any form of policies today so number one okay great so I'd say about half anyone using policy as code and kind of G Ops related okay about a third uh what about compliances code do anyone using is that today all right we have a couple of early adopters fantastic and then one other uh question what are your top pain points for Kuan needs policy Andor governance so number one deciding on which policy engine to use is that a pain point no okay everyone has seems to have that uh challenge
