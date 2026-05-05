---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Security", "GitOps Delivery", "SRE Reliability"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQgF/flux-secure-and-scalable-gitops-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Flux%3A+Secure+and+Scalable+GitOps+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Flux: Secure and Scalable GitOps | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]], [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQgF/flux-secure-and-scalable-gitops-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Flux%3A+Secure+and+Scalable+GitOps+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Flux: Secure and Scalable GitOps | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQgF/flux-secure-and-scalable-gitops-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Flux%3A+Secure+and+Scalable+GitOps+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LTwJIMWovO4
- YouTube title: Flux: Secure and Scalable GitOps | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/flux-secure-and-scalable-gitops-project-lightning-talk/LTwJIMWovO4.txt
- Transcript chars: 7241
- Keywords: flux, flagger, support, security, cluster, delivery, declarative, lightning, source, canary, reliability, continuous, environments, bootstrap, multiple, secure, scalable, provides

### Resumo baseado na transcript

all right oh we're excited all right great welcome to the flux project lightning talk hey yeah hi friends hey all right um and flux provides uh secure and scalable G Ops is this it yeah I mean if you don't already know tommo this is tommo and I'm Lee by the way I'm tommo yeah so but yeah we're the uh here at the flux uh Flux Lightning talk and we also have Flagger right yes we put our names at the end so I'm Tom nakahara um I

### Excerpt da transcript

all right oh we're excited all right great welcome to the flux project lightning talk hey yeah hi friends hey all right um and flux provides uh secure and scalable G Ops is this it yeah I mean if you don't already know tommo this is tommo and I'm Lee by the way I'm tommo yeah so but yeah we're the uh here at the flux uh Flux Lightning talk and we also have Flagger right yes we put our names at the end so I'm Tom nakahara um I guess my hat is community manager XXX yeah uh I'm Lee I work in R&D at on tanzu excellent yeah um so what is flux and in parentheses Flagger which is a sub project um so flux is really the project that created the term git Ops which the short term is um operations by pull request so basically flux really leverages the power of kubernetes it listens to your repo you have a yaml file that defines the single source of truth of your cluster and then when it notices a change it tells kubernetes oh please make sure that the cluster looks like what's in the ammo file so if any bad agents on the outside try to make changes um it'll completely get um overwritten um and Flagger is also a sub project of flux that provides um Progressive delivery like Canary deployments uh in between that process which will explain a little bit more um so it is a graduated project as you know um we also have General availability and uh security scale and reliability are Central to flux because many many Enterprises such as financial institutions government many more rely on flux and many of the vendors such as Microsoft AWS gitlab all rely on flux under the hood to provide git Ops to their customers yeah so what is under the hood yeah um a bunch of a bunch of components and pieces that you can really depend on I love that you mentioned that we've made the push in the flux project to hit General availability uh because when you consider being that level of production ready with the with the number of promises that we're making across all of our apis and all of our features um to say that flux is generally available is a huge accomplishment so thank you to anybody in this room who has helped us uh either as a user providing feedback uh or as somebody who has gotten our apis uh to that Finish Line uh as you know contributor to the project thank you so much uh flux is built with security scalability and reliability in mind uh we Implement flux as a series of microservices uh several controllers own all of the individual pieces uh that you need to have a sophisticated
