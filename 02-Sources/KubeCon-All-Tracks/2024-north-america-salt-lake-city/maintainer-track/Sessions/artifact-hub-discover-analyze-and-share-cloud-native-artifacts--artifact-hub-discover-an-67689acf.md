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
speakers: ["Matt Farina", "SUSE"]
sched_url: https://kccncna2024.sched.com/event/1howN/artifact-hub-discover-analyze-and-share-cloud-native-artifacts-matt-farina-suse
youtube_search_url: https://www.youtube.com/results?search_query=Artifact+Hub%3A+Discover%2C+Analyze%2C+and+Share+Cloud+Native+Artifacts+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Artifact Hub: Discover, Analyze, and Share Cloud Native Artifacts - Matt Farina, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Matt Farina, SUSE
- Schedule: https://kccncna2024.sched.com/event/1howN/artifact-hub-discover-analyze-and-share-cloud-native-artifacts-matt-farina-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Artifact+Hub%3A+Discover%2C+Analyze%2C+and+Share+Cloud+Native+Artifacts+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Artifact Hub: Discover, Analyze, and Share Cloud Native Artifacts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howN/artifact-hub-discover-analyze-and-share-cloud-native-artifacts-matt-farina-suse
- YouTube search: https://www.youtube.com/results?search_query=Artifact+Hub%3A+Discover%2C+Analyze%2C+and+Share+Cloud+Native+Artifacts+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=027rAkswODw
- YouTube title: Artifact Hub: Discover, Analyze, and Share Cloud Native Artifacts - Matt Farina, SUSE
- Match score: 0.959
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/artifact-hub-discover-analyze-and-share-cloud-native-artifacts/027rAkswODw.txt
- Transcript chars: 35956
- Keywords: artifact, search, artifacts, information, charts, projects, around, control, everything, actually, install, available, anybody, source, images, company, sidebar, listed

### Resumo baseado na transcript

all right hello everyone thank you for coming um today I'm going to talk about artifact Hub and uh one of the things that I'll tell you is I've got a lot of slides because artifact Hub is very Visual and so if you want to get the slides afterwards there will be a link at the end if I fly by them too quickly all right so have you ever searched for an app that you want to run in kubernetes maybe one of those things that you want and this system didn't scale in fact at one point it took like 30 seconds for this to load to display the few thousand of them we had because it was designed for something small and we needed a new system that could handle the scale of charts going out right and it was powered by software called binocular um now archive that had had been developed really for on Prem Solutions it was not designed for cloud scale or you know web scale or those kinds of things it

### Excerpt da transcript

all right hello everyone thank you for coming um today I'm going to talk about artifact Hub and uh one of the things that I'll tell you is I've got a lot of slides because artifact Hub is very Visual and so if you want to get the slides afterwards there will be a link at the end if I fly by them too quickly all right so have you ever searched for an app that you want to run in kubernetes maybe one of those things that you want to grab something off the shelf and just run somebody else's stuff and you go try to find it in a general search engine odds are you're going to have a hard time because there's going to be lots of stuff it's going to find they'll find blog posts on it tutorials and other things on it and maybe you know in this case you know you're looking for a Helm chart or a container or something but maybe you're also looking for something else like a policy you want to have policies around it right there's lots of policy engines these days and you might want a policy that's going to help you control some of that stuff try and find a policy and when you go to the search engines it can be pretty hard to find those those things right they're generic they're designed to give you everything out there they're designed to give you things like you know what's the latest maybe not what's the most useful or been around and the most solid they've got their own algorithms for it so how do you find those things and this is where artifact Hub comes in because there was a problem finding these kinds of distributed things out there that many of the projects and people are using and distributing and that's where artifact Cub came in to solve that problem um and you know what you know just to make it easy to find but it didn't just do it for one or two things we looked at a lot of things and said there's all of this different stuff out there right these are the different kinds of artifacts that can be discovered through artifact Hub today you'll see things like there's three different policy engines out there and they're policies there's kyno there's Opa gatekeeper and there's cubon right you'll see container images Helm charts there's plugins for various systems um there's tecton right stuff for t 10 what you're doing in this Cloud native space how do you find it when it's distributed all over the place and this is a centralized store to do that now it can be run on its own but we also have artifact hub.io and so it came together to find all these types um but I
