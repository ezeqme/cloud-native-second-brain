---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Kubernetes Core", "Sustainability", "Community Governance"]
speakers: ["Dan Sover", "Alex Greene", "Red Hat"]
sched_url: https://kccnceu2021.sched.com/event/iE6y/olm-a-declarative-way-to-install-manage-and-upgrade-operators-dan-sover-alex-greene-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=OLM%3A+A+Declarative+Way+to+Install%2C+Manage%2C+and+Upgrade+Operators+CNCF+KubeCon+2021
slides: []
status: parsed
---

# OLM: A Declarative Way to Install, Manage, and Upgrade Operators - Dan Sover & Alex Greene, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Sustainability]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Dan Sover, Alex Greene, Red Hat
- Schedule: https://kccnceu2021.sched.com/event/iE6y/olm-a-declarative-way-to-install-manage-and-upgrade-operators-dan-sover-alex-greene-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=OLM%3A+A+Declarative+Way+to+Install%2C+Manage%2C+and+Upgrade+Operators+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre OLM: A Declarative Way to Install, Manage, and Upgrade Operators.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE6y/olm-a-declarative-way-to-install-manage-and-upgrade-operators-dan-sover-alex-greene-red-hat
- YouTube search: https://www.youtube.com/results?search_query=OLM%3A+A+Declarative+Way+to+Install%2C+Manage%2C+and+Upgrade+Operators+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2iFbfPWNjYE
- YouTube title: OLM: A Declarative Way to Install, Manage, and Upgrade Operators - Dan Sover & Alex Greene, Red Hat
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/olm-a-declarative-way-to-install-manage-and-upgrade-operators/2iFbfPWNjYE.txt
- Transcript chars: 19145
- Keywords: operator, operators, cluster, bundle, resources, bundles, install, available, resource, manifests, container, application, information, custom, basically, manage, database, around

### Resumo baseado na transcript

hello everyone thank you for attending our kubecon eu 2021 presentation where we will be covering the operator lifecycle manager project commonly referred to as olm my name is alexander green and i'm a senior software developer working at red hat primarily focusing on the operator lifecycle manager project my teammate dan is also a developer for the olm team in today's presentation dan and i are briefly going to introduce the concept of a kubernetes operator discuss some of the challenges associated with managing a kubernetes operator as it

### Excerpt da transcript

hello everyone thank you for attending our kubecon eu 2021 presentation where we will be covering the operator lifecycle manager project commonly referred to as olm my name is alexander green and i'm a senior software developer working at red hat primarily focusing on the operator lifecycle manager project my teammate dan is also a developer for the olm team in today's presentation dan and i are briefly going to introduce the concept of a kubernetes operator discuss some of the challenges associated with managing a kubernetes operator as it evolved over the course of its lifetime and finally introduce some of the features that olm includes that makes it easier to manage these resources so typically we rely on kubernetes for deployment scaling and management of applications but at the end of the day we really just want to have a service available to our engineers or our customers take for example the classic mysql application on kubernetes mysql is a relational database management system that consists of both state full and stateless applications if you take a look at the resources at the bottom of the slide you'll see a deployment channel a service a persistent volume and a persistent volume claim as a developer with limited my sequel experience it's fairly easy for me to get a my sequel service up and running on my cluster by just creating four kubernetes resources unfortunately there are a few shortcomings with this approach first each of these resources are independently managed i don't really want to manage each of these resources on my own and when i have a disruption to my my sequel services i won't immediately know where to look i might have to look if the deployment came down or the service itself was deleted i might have to see if the persistent volume or persistent volume claim encountered an issue it would be much better if i could look at a single resource to identify what's going on with my mysql application perhaps more importantly i don't actually know how to safely perform an upgrade to a mysql database now certain i could devote a lot more of my time to understanding my sql to understanding how the upgrade should be performed and make it safely happen but i would much rather leave it to domain area experts to codify and handle this upgrade path and this is where operators really come into focus operators allow domain area experts to codify operational knowledge and software life cycles into an operator this operator exposes a kubernetes ap
