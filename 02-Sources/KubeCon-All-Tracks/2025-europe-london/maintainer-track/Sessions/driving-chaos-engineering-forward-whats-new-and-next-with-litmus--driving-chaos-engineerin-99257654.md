---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Sarthak Jain", "Saranya Jena", "Harness"]
sched_url: https://kccnceu2025.sched.com/event/1td04/driving-chaos-engineering-forward-whats-new-and-next-with-litmuschaos-sarthak-jain-saranya-jena-harness
youtube_search_url: https://www.youtube.com/results?search_query=Driving+Chaos+Engineering+Forward%3A+What%E2%80%99s+New+and+Next+With+LitmusChaos+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Driving Chaos Engineering Forward: What’s New and Next With LitmusChaos - Sarthak Jain & Saranya Jena, Harness

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Sarthak Jain, Saranya Jena, Harness
- Schedule: https://kccnceu2025.sched.com/event/1td04/driving-chaos-engineering-forward-whats-new-and-next-with-litmuschaos-sarthak-jain-saranya-jena-harness
- Busca YouTube: https://www.youtube.com/results?search_query=Driving+Chaos+Engineering+Forward%3A+What%E2%80%99s+New+and+Next+With+LitmusChaos+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Driving Chaos Engineering Forward: What’s New and Next With LitmusChaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1td04/driving-chaos-engineering-forward-whats-new-and-next-with-litmuschaos-sarthak-jain-saranya-jena-harness
- YouTube search: https://www.youtube.com/results?search_query=Driving+Chaos+Engineering+Forward%3A+What%E2%80%99s+New+and+Next+With+LitmusChaos+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6GjLzWtqjlw
- YouTube title: Driving Chaos Engineering Forward: What’s New and Next With LitmusCha... Sarthak Jain & Saranya Jena
- Match score: 0.92
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/driving-chaos-engineering-forward-whats-new-and-next-with-litmuschaos/6GjLzWtqjlw.txt
- Transcript chars: 25774
- Keywords: support, litmas, litmus, experiment, security, application, multiple, basically, probes, faults, experiments, planning, coming, secure, adding, working, infrastructure, control

### Resumo baseado na transcript

hey everyone good afternoon um uh welcome to today's session on driving Kos engineering forward what's new and next with litmus chaos so in this talk we'll be uh sharing what's going on with litmus what we have been working on uh what are the road map items and what we have achieved so far so yeah uh a bit of intro about myself uh this is sna and I am a senior software engineer at harness and also one of the maintainers of lmus chos so yeah I'll give

### Excerpt da transcript

hey everyone good afternoon um uh welcome to today's session on driving Kos engineering forward what's new and next with litmus chaos so in this talk we'll be uh sharing what's going on with litmus what we have been working on uh what are the road map items and what we have achieved so far so yeah uh a bit of intro about myself uh this is sna and I am a senior software engineer at harness and also one of the maintainers of lmus chos so yeah I'll give the hi good afternoon everyone I am sarak Jan and I a senior software engineer at harness as well and also a maintainer of litmus Kos right so litmas Kos is a cncf incubating project which allows users to practice Kos engineering on their Cloud native applications and it has a mission of making Kos engineering secure as well as accessible so Kos engineering basically verifies the resilience of a business services and helps devops pipelines build code that is more resilient against software and infrastructure faults all right so here's a timeline and what has happened with litmus chos from cucon to cubec con I hope it is uh visible uh but I'll still read read it out for you guys so it all started in 2018 so lmus chos was first announced announced in cucon na 2018 at that time it was completely anible based so Kos experiments were um executed based on some scripts and lus Kos only had some basic pod level faults in cucon Europe 2019 Kos operator was launched so Kos operator is basically a tool that is used to manage and orchestrate chos falls into the users's cluster uh chos operator basically manages the complete life cycle of of The chos Happening into the users's cluster we also introduced chos crds that is the custom resource definitions for Kos and from ncel we migrated to goang so we migrated to golang the reason was it had better support for what we were trying to build and also for better um you know adoption and moving to cucon na 2019 principles of cnce was published CNC is basically Cloud native uh chos engineering so uh this was published and uh we launched Kos Hub so Kos Hub is um basically a hub which consists of all the chos faults that are available so users can just browse through the Hub check the list of the faults that are available and um use them according to their use case we also added support for byoc byoc is bring your own Kos so just in case um you know the the list of faults that is not enough for someone in the Kos sub they can anytime go and create their own own Kos fault and add it
