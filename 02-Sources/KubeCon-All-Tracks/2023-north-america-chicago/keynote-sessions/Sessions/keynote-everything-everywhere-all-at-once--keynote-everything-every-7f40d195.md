---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Keynote Sessions"
themes: ["AI ML", "Storage Data"]
speakers: ["Hemanth Malla", "Senior Software Engineer", "Datadog", "Laurent Bernaille", "Principal Engineer", "Datadog"]
sched_url: https://kccncna2023.sched.com/event/1R4bN/keynote-everything-everywhere-all-at-once-hemanth-malla-senior-software-engineer-datadog-laurent-bernaille-principal-engineer-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Everything%2C+Everywhere%2C+All+At+Once+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keynote: Everything, Everywhere, All At Once - Hemanth Malla, Senior Software Engineer, Datadog & Laurent Bernaille, Principal Engineer, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: United States / Chicago
- Speakers: Hemanth Malla, Senior Software Engineer, Datadog, Laurent Bernaille, Principal Engineer, Datadog
- Schedule: https://kccncna2023.sched.com/event/1R4bN/keynote-everything-everywhere-all-at-once-hemanth-malla-senior-software-engineer-datadog-laurent-bernaille-principal-engineer-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Everything%2C+Everywhere%2C+All+At+Once+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keynote: Everything, Everywhere, All At Once.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R4bN/keynote-everything-everywhere-all-at-once-hemanth-malla-senior-software-engineer-datadog-laurent-bernaille-principal-engineer-datadog
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Everything%2C+Everywhere%2C+All+At+Once+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Q9P--Fr1XRo
- YouTube title: Keynote: Everything, Everywhere, All At Once - Hemanth Malla & Laurent Bernaille
- Match score: 0.799
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keynote-everything-everywhere-all-at-once/Q9P--Fr1XRo.txt
- Transcript chars: 14672
- Keywords: network, incident, course, actually, recover, started, wanted, networking, instances, pretty, unattended, discovered, restart, instance, however, clusters, platform, happening

### Resumo baseado na transcript

welcome to day two of cubec Con Chicago it's great to be here my name is hant and today we're here to talk to you about the hardest incident we ever had to deal with at data dog what is data dog data dog is a cloud monitoring security and observability Company and at data dog we run kubernetes at a large scale we run hundreds of self-managed kubernetes clusters which help us manage tens of thousands of kubernetes nodes and some of our kubernetes clusters have 4,000 plus nodes

### Excerpt da transcript

welcome to day two of cubec Con Chicago it's great to be here my name is hant and today we're here to talk to you about the hardest incident we ever had to deal with at data dog what is data dog data dog is a cloud monitoring security and observability Company and at data dog we run kubernetes at a large scale we run hundreds of self-managed kubernetes clusters which help us manage tens of thousands of kubernetes nodes and some of our kubernetes clusters have 4,000 plus nodes in them so what happened what was this hardest incident so on March 8th 2023 our platform experienced a global outage and our users were unable to access the platform for around 10 hours and it would take us another 12 hours to recover the last major service and this happened because we lost 60% of our compute capacity across multiple Cloud providers Distributing in several availability zones in a span of 1 hour this is a story of how we lost almost everything everywhere all at once at data dog so during the incident our internal data dog employees realized that they were not able to access the kubernetes control ples and our admin teams were having trouble trying to even as into the nodes to try and debug what was happening so at this point it seemed like a widespread Network outage so did we roll out a bad change fleetwide no we actually have explicit policies in place to prevent our Engineers from deploying code too fast so how did this happen in fact we run completely independent Stacks with no explicit dependencies between them so there's no way we could have deployed something that can impact all of our data centers at the same time luckily for us at data dog we have a strong culture of incident response so it was pretty easy for us to get all hands on deck pretty quickly our Engineers who build these Services own them end to end and as you can see from the screenshot we were having around 400 plus Engineers working in different breakout rooms trying to figure out what was happening soon enough one of our Engineers figured out that we were able to recover some of the Lost nodes by simply restarting them from Google Cloud console or via the GC API and once we recovered those nodes we were able to SSH into them and take a closer look at the system logs and that system logs told us that there was an unattended upgrade on these nodes and soon after the unattended upgrade these nodes were losing network connectivity so what are unattended upgrades unattended upgrades are our Legacy w
