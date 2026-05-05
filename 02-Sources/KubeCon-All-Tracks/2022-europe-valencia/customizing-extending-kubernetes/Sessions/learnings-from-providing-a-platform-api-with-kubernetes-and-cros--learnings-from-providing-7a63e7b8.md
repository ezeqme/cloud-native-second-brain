---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Hannes Blut", "Jan Willies", "Accenture"]
sched_url: https://kccnceu2022.sched.com/event/ytny/learnings-from-providing-a-platform-api-with-kubernetes-and-crossplane-hannes-blut-jan-willies-accenture
youtube_search_url: https://www.youtube.com/results?search_query=Learnings+From+Providing+A+Platform+API+With+Kubernetes+And+Crossplane+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Learnings From Providing A Platform API With Kubernetes And Crossplane - Hannes Blut & Jan Willies, Accenture

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Hannes Blut, Jan Willies, Accenture
- Schedule: https://kccnceu2022.sched.com/event/ytny/learnings-from-providing-a-platform-api-with-kubernetes-and-crossplane-hannes-blut-jan-willies-accenture
- Busca YouTube: https://www.youtube.com/results?search_query=Learnings+From+Providing+A+Platform+API+With+Kubernetes+And+Crossplane+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Learnings From Providing A Platform API With Kubernetes And Crossplane.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytny/learnings-from-providing-a-platform-api-with-kubernetes-and-crossplane-hannes-blut-jan-willies-accenture
- YouTube search: https://www.youtube.com/results?search_query=Learnings+From+Providing+A+Platform+API+With+Kubernetes+And+Crossplane+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XyR9DGnOpXo
- YouTube title: Learnings From Providing A Platform API With Kubernetes And Crossplane - Hannes Blut & Jan Willies
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/learnings-from-providing-a-platform-api-with-kubernetes-and-crossplane/XyR9DGnOpXo.txt
- Transcript chars: 23649
- Keywords: cluster, crossplane, provider, application, platform, running, however, resources, probably, infrastructure, clusters, compliant, deploy, central, controllers, create, bottom, object

### Resumo baseado na transcript

all right welcome everybody to our talk on kubernetes and crossplane and building a platform api on top of kubernetes so there are still some free seats available here in the front on the right side and a couple there on the left if you don't want to stand in the back and well today we want to talk about our experience in adopting kubernetes controllers for managing things who are not core kubernetes controllers and we are doing that with a cncf project called crossplane and they have quite

### Excerpt da transcript

all right welcome everybody to our talk on kubernetes and crossplane and building a platform api on top of kubernetes so there are still some free seats available here in the front on the right side and a couple there on the left if you don't want to stand in the back and well today we want to talk about our experience in adopting kubernetes controllers for managing things who are not core kubernetes controllers and we are doing that with a cncf project called crossplane and they have quite the presence here so i want to have a quick show fans who has heard of crossplane before all right all right so it's hard to not uh hard to ignore crossplane at this conference that's for sure and that's good so we'll start with a quick intro uh who who we are uh michael lecanis maybe you want to go first yeah my name is hans blut i i'm a cloud architect at accenture and i live in frankfurt germany my name is jan vegas i live in berlin i'm a platform architect accenture i do uh i do most of the stuff i do is open source i'm a contributor to the crossplane project i do also do the valencia icd meetup so if you're in berlin and if you are interested in in in connecting and with other folks who are running cicd then feel free to reach out it's been on hiatus for the past two years due to some pandemic events but we plan to pick it up this summer again and we are also managing the foster mci cd dev room so if you are joining foster in brussels hopefully in presence next year um feel free to catch us and the cicd deaf room all right so a very quick introduction crossplane so probably you've by now heard many intros to crossplane uh this is uh this might be the third one but let me quickly explain in layman's terms so what crossplane does it extends a service provider apis which are pictured here at the bottom into the kubernetes resource model into the kubernetes database so a as a user i can cube cd get clusters and i do get my eks cluster back from aws similar i can create kubernetes clusters via [Music] via the kubernetes platform so i just apply a familial yammer and there's a controller running who takes this yaml representation and talks to the aws api via aws go sdk and manage the state at aws for me it continuously does so so that's the kubernetes pattern the reconciliation uh every well it's configurable but every 60 seconds by default so if there's any any drift or any changes then those are overwritten or updated to the state which i want to give that so this is a
