---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Vladik Romanovsky", "David Vossel", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1hoy6/kubevirt-enhancements-and-the-road-ahead-vladik-romanovsky-david-vossel-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=KubeVirt%3A+Enhancements+and+the+Road+Ahead+CNCF+KubeCon+2024
slides: []
status: parsed
---

# KubeVirt: Enhancements and the Road Ahead - Vladik Romanovsky & David Vossel, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Vladik Romanovsky, David Vossel, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1hoy6/kubevirt-enhancements-and-the-road-ahead-vladik-romanovsky-david-vossel-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=KubeVirt%3A+Enhancements+and+the+Road+Ahead+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre KubeVirt: Enhancements and the Road Ahead.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoy6/kubevirt-enhancements-and-the-road-ahead-vladik-romanovsky-david-vossel-red-hat
- YouTube search: https://www.youtube.com/results?search_query=KubeVirt%3A+Enhancements+and+the+Road+Ahead+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LfLahyTIIc8
- YouTube title: KubeVirt: Enhancements and the Road Ahead - Vladik Romanovsky & David Vossel, Red Hat
- Match score: 0.752
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kubevirt-enhancements-and-the-road-ahead/LfLahyTIIc8.txt
- Transcript chars: 23048
- Keywords: cubert, migration, virtual, machine, actually, another, change, target, features, working, effectively, operator, cluster, object, running, volumes, resources, scheduling

### Resumo baseado na transcript

my name is VL Romanowski I'm one of the maintainers of the cubert project and today I would like to share some of the progress that kber had over the past year both in terms of features uh but also the community work um for those who are not familiar um cubert is an operator that extends the uh um kubernetes API server to allow users uh to run virtual machines alongside the uh pods and uh this is all uh using the same uh familiar kubernetes API um we

### Excerpt da transcript

my name is VL Romanowski I'm one of the maintainers of the cubert project and today I would like to share some of the progress that kber had over the past year both in terms of features uh but also the community work um for those who are not familiar um cubert is an operator that extends the uh um kubernetes API server to allow users uh to run virtual machines alongside the uh pods and uh this is all uh using the same uh familiar kubernetes API um we run the uh qmu process that emulates the virtual machine inside a container um as you would normally do with any other user space application um it's often viewed uh kubert is often viewed uh by some as a replacement for other rutilization platforms however um cubert is significantly much more it's uh integrates deeply with the um with kubernetes and we reuse multiple um Native um kubernetes components in cubert and uh cubert is actually part of a a broader kubernetes ecosystem uh where it can be a component in a pipeline or provide uh a way to craft interesting Solutions uh using it one such solution is uh uh is the cubert provider for cluster API where um cubert virtual machines are being used as as nodes um for virtual kubernetes clusters this was a good year uh for cubert to um in general lots of different companies were interested in the in it and um here's a compilation of some that added themselves as a um as adopters in terms of community work um as kubert matures uh code quality takes the central stage and uh it becomes a Hot Topic in in the community uh this year we have been also uh working on evolving our sigs and uh creating uh working groups and the sub projects and um this is not just in terms of code separation to different areas uh but also we went ahead and created this these groups of people um groups of contributors uh that are interested in a specific area and will become expert in it uh but also they will take responsibility um for fixing uh bugs in that area and uh and generally maintaining uh qu quality there this step also allows our contributors to evolve within the project um so anywhere from um being reviewers um contributors can become uh approvers in the specific F Sig and then become uh chairs afterwards um they can grow in being um uh brute level approver for the whole um for the whole project uh but also eventually they can grow uh to become maintainers um this year we also established our um future life cycle uh policy something that we didn't have before and uh similar to kub
