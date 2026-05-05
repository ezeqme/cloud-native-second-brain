---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Unclassified"
themes: ["Kubernetes Core"]
speakers: ["Madhuri Yechuri", "Elotl", "Zach Gray", "Flare.build"]
sched_url: https://kccnceu2022.sched.com/event/ytlw/kubernetes-for-mac-how-to-consume-shiny-aws-mac-shapes-for-ios-builds-madhuri-yechuri-elotl-zach-gray-flarebuild
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+for+Mac%3A+How+to+Consume+Shiny+AWS+Mac+Shapes+for+iOS+Builds+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kubernetes for Mac: How to Consume Shiny AWS Mac Shapes for iOS Builds - Madhuri Yechuri, Elotl & Zach Gray, Flare.build

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Madhuri Yechuri, Elotl, Zach Gray, Flare.build
- Schedule: https://kccnceu2022.sched.com/event/ytlw/kubernetes-for-mac-how-to-consume-shiny-aws-mac-shapes-for-ios-builds-madhuri-yechuri-elotl-zach-gray-flarebuild
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+for+Mac%3A+How+to+Consume+Shiny+AWS+Mac+Shapes+for+iOS+Builds+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kubernetes for Mac: How to Consume Shiny AWS Mac Shapes for iOS Builds.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytlw/kubernetes-for-mac-how-to-consume-shiny-aws-mac-shapes-for-ios-builds-madhuri-yechuri-elotl-zach-gray-flarebuild
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+for+Mac%3A+How+to+Consume+Shiny+AWS+Mac+Shapes+for+iOS+Builds+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LQOC8vI20eU
- YouTube title: Kubernetes for Mac: How to Consume Shiny AWS Mac Shapes for iOS Builds - Madhuri Yechuri & Zach Gray
- Match score: 0.921
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kubernetes-for-mac-how-to-consume-shiny-aws-mac-shapes-for-ios-builds/LQOC8vI20eU.txt
- Transcript chars: 34832
- Keywords: course, compute, pending, running, instances, scaling, agents, nodeless, config, little, actually, managed, actions, manually, builds, scalar, instance, workload

### Resumo baseado na transcript

hello everyone welcome to our little talk um so obviously as you've seen from the title here we're going to talk about something pretty exciting uh which is um consuming mac os compute inside of kubernetes um so this is something that we're super excited to talk about so today um you'll be hearing both from myself and for my co-host madri and so we're respectively you know working at the companies that you see up here and so a little bit about myself and flair to kick things off

### Excerpt da transcript

hello everyone welcome to our little talk um so obviously as you've seen from the title here we're going to talk about something pretty exciting uh which is um consuming mac os compute inside of kubernetes um so this is something that we're super excited to talk about so today um you'll be hearing both from myself and for my co-host madri and so we're respectively you know working at the companies that you see up here and so a little bit about myself and flair to kick things off so yeah a little bit about flare so you have to forgive me for looking up at the screen there's no mirroring here so um yeah a little bit about flair we're part of bazel's experts program which is a community program organized by google um to sort of connect uh you know folks in the bazel ecosystem with expert help um so uh you know we do a lot of bazel consultancy uh working with a lot of large organizations um another thing that we do is we actually offer um some value-added services uh in sort of a sas or infrastructure as a service model to folks using bazel to build and test applications at scale so we'll dive in a little bit into bazel i won't go too deep i don't want to bore you too much but um suffice it to say bazel is a is a great build tool um that you know connects to you know remote clusters to do distributed builds um and that's you know sort of the focus of my company flair and so you know one of the challenges here is we build these big distributed systems to do distributed builds we also have to deal with um sort of unifying lots of different compute types so you know for example mac os when we're doing ios builds so there's a lot of underlying complexity here to the product that we're building and so we're of course thrilled to have partnered up with a loadle to help us with some of the underlying infrastructure stuff so we can really focus on building out our product and so with that madre do you want to introduce yourself i'm madri i'm founder of ilotal makers of nodeless kubernetes the vision for nodeless communities is we have transitioned from treating applications as pets to treating applications as cattle the vision for nodeless is to do the same for compute so not to have pre-provisioned always on compute that's hand curated but compute that comes up and disappears according to application life cycle so it falls in it works in two levels the first level is at a single cluster where you just have a kubernetes control plane that is deployed and no compute th
