---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Nick Beenham", "Comcast", "Jonathan Smith", "Microsoft"]
sched_url: https://kccncna2025.sched.com/event/27Fbe/how-comcast-leverages-radius-in-their-internal-developer-platform-nick-beenham-comcast-jonathan-smith-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=How+Comcast+Leverages+Radius+in+Their+Internal+Developer+Platform+CNCF+KubeCon+2025
slides: []
status: parsed
---

# How Comcast Leverages Radius in Their Internal Developer Platform - Nick Beenham, Comcast & Jonathan Smith, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Nick Beenham, Comcast, Jonathan Smith, Microsoft
- Schedule: https://kccncna2025.sched.com/event/27Fbe/how-comcast-leverages-radius-in-their-internal-developer-platform-nick-beenham-comcast-jonathan-smith-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=How+Comcast+Leverages+Radius+in+Their+Internal+Developer+Platform+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre How Comcast Leverages Radius in Their Internal Developer Platform.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fbe/how-comcast-leverages-radius-in-their-internal-developer-platform-nick-beenham-comcast-jonathan-smith-microsoft
- YouTube search: https://www.youtube.com/results?search_query=How+Comcast+Leverages+Radius+in+Their+Internal+Developer+Platform+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=axR7paIbmPI
- YouTube title: How Comcast Leverages Radius in Their Internal Developer Platform - Nick Beenham & Jonathan Smith
- Match score: 0.903
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/how-comcast-leverages-radius-in-their-internal-developer-platform/axR7paIbmPI.txt
- Transcript chars: 25561
- Keywords: radius, application, developer, platform, resource, comcast, resources, define, thanks, deploy, terraform, developers, number, projects, contributions, custom, control, together

### Resumo baseado na transcript

Uh I became involved with the Radius program towards the end of 2023 and this is a a bit of a talk about how we sort of see Radius at Comcast and the potential and how we want to sort of maybe integrate this into our developer platform. So, we're the team that created Radius and contributed Radius and a number of other projects uh to the CNCF. So uh Radius runs and deploys applications Kubernetes leverages Terraform has uh tight integration with Dapper um is integrated with popular GitOps tools like Flux um Argo CD in the backlog a backstage there's a um there's a radius plugin in the in the pipeline There's a a number of questions that that Radius kind of seeks to answer in the context of developer and platform engineering challenges that that are listed here. Namely, um how can we help um platform engineers working with developers to maximize productivity without developers getting too bogged down in the complexities uh of Kubernetes? whether that's a Kubernetes resource um or services from different cloud providers like AWS and Azure um how can we help platform engineers enforce things like security um operations and cost containment best practices without putting too many um kind of ownorous constraints on application developers.

### Excerpt da transcript

My name is Nick Beam. Uh I'm a distinguished engineer at Comcast. Uh I became involved with the Radius program towards the end of 2023 and this is a a bit of a talk about how we sort of see Radius at Comcast and the potential and how we want to sort of maybe integrate this into our developer platform. >> Great. I'm Jonathan Smith. I run product management for the Azure Opensource Incubations team. So, we're the team that created Radius and contributed Radius and a number of other projects uh to the CNCF. Um, and I'm happy to be on stage with with Nick. He's our superstar uh community member, sort of leading the pack in terms of contributions to Radius. And we're hoping that more folks in the room here as you learn about Radius will will follow in in Nick's uh illustrious footsteps. Um, I'll provide a little bit of context um about Radius and the incubations team. And then really the the bulk of the content today is is Nick talking about how Comcast um is using Radius. So the Azure incubations team has a mission to work across the open source community uh to find to deliver technologies that help accelerate our collective journey to the cloud.

Right? So we don't focus just on Azure customers or um or Microsoft customers um but we look at the industry uh at large and because we're working with the industry at large to accelerate everyone's migration to cloud our ship vehicle is open source and since our ship vehicle is open source we partner with the CNCF. So once we have a project that we think has value and has legs that we've been incubating, uh then we contribute that project to the CNCF. Uh and they've just been great partners in terms of building uh community around the projects um and helping drive our open um governance approach. So so that's been a great partnership. Most folks that I talk to at CubeCon are familiar with some of the projects that come out of Azure incubations. In particular, Kada and Dapper um are are projects that folks are tend to be familiar with. A lot of times folks don't realize that those two projects came from the same team. uh and and oftentimes I also don't realize there's a pipeline of projects coming out of this organization including Radius which we'll talk about today but also Copathetic um which you see in the the bottom left um corner of this this portfolio slide and DRSI as well which is a cool project um that hopefully you'll join me right after this presentation we'll be going downstairs to see um a presentation
