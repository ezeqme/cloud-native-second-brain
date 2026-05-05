---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Customizing + Extending Kubernetes"
themes: ["GitOps Delivery", "Kubernetes Core"]
speakers: ["Jesse Suen", "Akuity", "Viktor Farcic", "Upbound"]
sched_url: https://kccncna2022.sched.com/event/182Hj/like-peas-and-carrots-argo-cd-and-crossplane-for-infrastructure-management-jesse-suen-akuity-viktor-farcic-upbound
youtube_search_url: https://www.youtube.com/results?search_query=Like+Peas+And+Carrots%3A+Argo+CD+And+Crossplane+For+Infrastructure+Management+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Like Peas And Carrots: Argo CD And Crossplane For Infrastructure Management - Jesse Suen, Akuity & Viktor Farcic, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Jesse Suen, Akuity, Viktor Farcic, Upbound
- Schedule: https://kccncna2022.sched.com/event/182Hj/like-peas-and-carrots-argo-cd-and-crossplane-for-infrastructure-management-jesse-suen-akuity-viktor-farcic-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=Like+Peas+And+Carrots%3A+Argo+CD+And+Crossplane+For+Infrastructure+Management+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Like Peas And Carrots: Argo CD And Crossplane For Infrastructure Management.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Hj/like-peas-and-carrots-argo-cd-and-crossplane-for-infrastructure-management-jesse-suen-akuity-viktor-farcic-upbound
- YouTube search: https://www.youtube.com/results?search_query=Like+Peas+And+Carrots%3A+Argo+CD+And+Crossplane+For+Infrastructure+Management+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=QO_-PG9snvI
- YouTube title: Like Peas And Carrots: Argo CD And Crossplane For Infrastructure Manag... Jesse Suen & Viktor Farcic
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/like-peas-and-carrots-argo-cd-and-crossplane-for-infrastructure-manage/QO_-PG9snvI.txt
- Transcript chars: 26401
- Keywords: composition, resources, cluster, argo, resource, add-ons, called, create, cross-plane, add-on, managed, probably, provider, manage, infrastructure, compositions, basically, feature

### Resumo baseado na transcript

uh thanks everyone for attending our talk on Cross plain and Argo CD my name is Jesse suan I'm one of the co-creators of the Argo project and co-founder of a company called Acuity which offers fully managed Argo CD in the cloud and speaking with me today is Victor who you probably already know from his very popular YouTube channel yeah so my name is Victor I work for a band a company behind cross plain and uh this is a bit difficult subject because we're talking about tips

### Excerpt da transcript

uh thanks everyone for attending our talk on Cross plain and Argo CD my name is Jesse suan I'm one of the co-creators of the Argo project and co-founder of a company called Acuity which offers fully managed Argo CD in the cloud and speaking with me today is Victor who you probably already know from his very popular YouTube channel yeah so my name is Victor I work for a band a company behind cross plain and uh this is a bit difficult subject because we're talking about tips and trips how many of you are using Crosman today the rest of you might have trouble to follow up this is going into into All the Troubles that this guy was facing with crosswind anyways so let me give you a very quick introduction very very quick introduction into um in into Cross Point right and uh I'm gonna show it in a way from from the point of uh view of History right uh at the very beginning uh we got confirmations uh management tools Chef puppet ansible you know all those things some of you are probably using our civil steel and they were all based on the idea that things are mutable right I know that they can do immutable things but based on mutable principles uh you can call that the first generation what later on became infrastructures code uh and they were they were mostly based for bare metal you know real servers you know before virtual machines and before cloud and all those things and then we got into the second generation of such tools that we called that second generation infrastructure is called it's called bit terraform pollummy cloud formation all the good stuff that many of you are probably using right now what is happening right now uh with the with the emerges of kubernetes is that we are moving into the next phase and that that next phase is using kubernetes as a control plane right using kubernetes with all the good things that we we all how many of you are not using kubernetes okay I'm just checking uh with all the good things and all the things you like right now extensible apis custom resource definitions Drive detection reconciliation and all the all the stuff that we like right and the whole idea is that uh thinking of kubernetes is something that runs containers is wrong right that that containers are just one of the implementations of kubernetes scheduler and we have many many many others and one of those others is cross play so what we're trying to do with crossplay can be uh described uh through two main areas right one area would be one-to-one matching
