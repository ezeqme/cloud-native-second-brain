---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: ["A Lightning Tour | Project Lightning Talk"]
sched_url: https://kccncna2024.sched.com/event/1iW8t/crossplane-the-many-layers-of-crossplane-a-lightning-tour-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Crossplane%3A+The+Many+Layers+of+Crossplane+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Crossplane: The Many Layers of Crossplane - A Lightning Tour | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Salt Lake City
- Speakers: A Lightning Tour | Project Lightning Talk
- Schedule: https://kccncna2024.sched.com/event/1iW8t/crossplane-the-many-layers-of-crossplane-a-lightning-tour-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Crossplane%3A+The+Many+Layers+of+Crossplane+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Crossplane: The Many Layers of Crossplane.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8t/crossplane-the-many-layers-of-crossplane-a-lightning-tour-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Crossplane%3A+The+Many+Layers+of+Crossplane+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=4sFrRMO_0JQ
- YouTube title: Crossplane: The Many Layers of Crossplane - A Lightning Tour | Project Lightning Talk
- Match score: 0.747
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/crossplane-the-many-layers-of-crossplane/4sFrRMO_0JQ.txt
- Transcript chars: 5803
- Keywords: crossplane, composition, control, developers, function, imagine, learning, developer, platform, asking, observability, around, faster, resources, standards, functions, single, anything

### Resumo baseado na transcript

all right everyone uh my name is Blake Romano I'm a senior software engineer at Imagine Learning building our internal developer platform and today I'm going to be talking through the many layers of crossplane and kind of give you a little lightning tour so you may be asking you know what is crossplane uh crossplane is a control plane framework um that is highly sensible and allows you to build platforms and based on kind of kubernetes and talk to various different Cloud providers uh Source Control Management tools

### Excerpt da transcript

all right everyone uh my name is Blake Romano I'm a senior software engineer at Imagine Learning building our internal developer platform and today I'm going to be talking through the many layers of crossplane and kind of give you a little lightning tour so you may be asking you know what is crossplane uh crossplane is a control plane framework um that is highly sensible and allows you to build platforms and based on kind of kubernetes and talk to various different Cloud providers uh Source Control Management tools observability tools um and build a control plane around that kind of using this framework so you know you may be asking great crossplane sounds cool why should I be using it um so coming from Imagine Learning which we're an education technology company we wanted to build an internal developer platform to help our developers you know deploy faster move faster and safer um so with with adoption of crossplane we've seen that deployments are actually happening about 80% faster um with crossplane to our Cloud resources um and this is due to the way we're able to abstract using crossplane using you know composition composite resource definitions which is similar to crds and we're also to be able to maintain security reliability and cost standards by being able to abtract away all the complexities that you know as a application developer you may say hey I don't really need to worry about encryption you know the platform can handle that for me so we're able to maintain all those standards by abstracting all those complexities away through compositions one other thing that we've able to do is written our control plane in a language that we we chose um so we're writing our control plane in goang and testing with you know kind of our normal coding standards and with some of the utilities that crossplane gives us by utilizing composition functions we're also able to reduce the complexity of continuous deployment because now kubernetes is our single deployment uh location we're only deploying things into kubernetes using crossplane and so now we only have a single CD pipeline for anything we may want to deploy in our world which grassly uh or vastly reduces the complexity um in crossplane in general one of the exciting things that has happened in the past 6 to 12 months is uh composition function have wga um this is super exciting news uh for somebody who loves composition functions um you're able to create pipelines where um you can use things like go templ
