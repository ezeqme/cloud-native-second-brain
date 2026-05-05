---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Nuno Guedes", "Millennium bcp", "Jonathan Smith", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1txHI/how-millennium-bcp-leverages-radius-to-empower-developer-+-operator-collaboration-nuno-guedes-millennium-bcp-jonathan-smith-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=How+Millennium+Bcp+Leverages+Radius+To+Empower+Developer+%2B+Operator+Collaboration+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How Millennium Bcp Leverages Radius To Empower Developer + Operator Collaboration - Nuno Guedes, Millennium bcp & Jonathan Smith, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Nuno Guedes, Millennium bcp, Jonathan Smith, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1txHI/how-millennium-bcp-leverages-radius-to-empower-developer-+-operator-collaboration-nuno-guedes-millennium-bcp-jonathan-smith-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=How+Millennium+Bcp+Leverages+Radius+To+Empower+Developer+%2B+Operator+Collaboration+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How Millennium Bcp Leverages Radius To Empower Developer + Operator Collaboration.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHI/how-millennium-bcp-leverages-radius-to-empower-developer-+-operator-collaboration-nuno-guedes-millennium-bcp-jonathan-smith-microsoft
- YouTube search: https://www.youtube.com/results?search_query=How+Millennium+Bcp+Leverages+Radius+To+Empower+Developer+%2B+Operator+Collaboration+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZmcZlDCYDgE
- YouTube title: How Millennium Bcp Leverages Radius To Empower Developer + Operator... Nuno Guedes & Jonathan Smith
- Match score: 0.91
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-millennium-bcp-leverages-radius-to-empower-developer-operator-coll/ZmcZlDCYDgE.txt
- Transcript chars: 23875
- Keywords: radius, application, resource, deploy, platform, developer, developers, deployed, container, infrastructure, custom, resources, deployment, recipe, feature, environment, source, premise

### Resumo baseado na transcript

Welcome to how Millennium BCP leverages radius to empower developer and operator collaboration. I work at well Millennium BCP and I'm the head of public cloud and with me I have I am Jonathan Smith. Um, and I get to work with a lot of platform engineers and they've taught me a ton about like the challenges they face and the platforms that they're building. And I think this uh graphic from Canoe um does a great job sort of laying out a canonical um reference architecture showing a lot of the common elements in an IDP um and a lot of the open source technologies that that serve those Um and that ambiguity uh in addition to all the other challenges around cloudnative development just adds that the cognitive load that developers struggle with and it's exactly that load that the IDPs are are designed and built um to address. So if it's a a cloud storage resource for example, the ability for a developer to just ask for a particular type of storage and say I need small, medium or large instead of lots of detailed configuration.

### Excerpt da transcript

Hello everyone. Welcome to how Millennium BCP leverages radius to empower developer and operator collaboration. I'm Nun. I work at well Millennium BCP and I'm the head of public cloud and with me I have I am Jonathan Smith. I'm the head of product management uh for the Azure open source incubations team at Microsoft and honored to be on stage with my friend and colleague Nuno. So first of all show of hands are you familiar with Radius besides the network protocol? Oh good nice. That's good. That's a star. We'll increase that number over the next 30 minutes. Do you want to share a bit about what this is? Sure. Sure. So, we will we'll do a couple of things here. I'll start off and give some basic context about what Radius is, some demos of how it works, and then Nuno will walk us through some of the cool work he's done at NBCP uh to adopt Radius as part of their internal developer platform, including getting workloads to production on Radius starting in last December. Um, so so here we go with some context then.

So, so as I mentioned, I'm in the Azure open source incubations team at Microsoft and we've donated um several projects to CNCF. Today, we're going to focus, as we said, on Radius. Um but hopefully you'll have a chance to take a look at some of the other projects that are listed here. Uh Dapper and Kada. There's a lot of folks that I talked to at CubeCon that are familiar with those. They're already graduated CNCF projects. There's newer projects I won't touch on here too much, but just take a look at Copacetic. you see in the lower left corner and DSI two new super interesting projects like everything else on the list here they are available uh freely on GitHub uh under the Apache 2.0 their license. So if you get a chance, check them out. So in the context of Radius, Nuno and I will talk mostly about Radius features that help platform engineers like his team uh build IDPs that better serve their their developer and operator customers. Um, and I get to work with a lot of platform engineers and they've taught me a ton about like the challenges they face and the platforms that they're building.

Um, and the way different open source technologies help accelerate that product development. And I think this uh graphic from Canoe um does a great job sort of laying out a canonical um reference architecture showing a lot of the common elements in an IDP um and a lot of the open source technologies that that serve those platforms and Nuno and I found common g
