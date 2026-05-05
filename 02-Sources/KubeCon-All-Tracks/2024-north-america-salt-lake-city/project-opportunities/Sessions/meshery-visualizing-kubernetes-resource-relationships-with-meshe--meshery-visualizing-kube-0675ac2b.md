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
themes: ["Kubernetes Core"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iWA9/meshery-visualizing-kubernetes-resource-relationships-with-meshery-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Meshery%3A+Visualizing+Kubernetes+Resource+Relationships+with+Meshery+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Meshery: Visualizing Kubernetes Resource Relationships with Meshery | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iWA9/meshery-visualizing-kubernetes-resource-relationships-with-meshery-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Meshery%3A+Visualizing+Kubernetes+Resource+Relationships+with+Meshery+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Meshery: Visualizing Kubernetes Resource Relationships with Meshery | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iWA9/meshery-visualizing-kubernetes-resource-relationships-with-meshery-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Meshery%3A+Visualizing+Kubernetes+Resource+Relationships+with+Meshery+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xJ9RH0AE7zE
- YouTube title: Meshery: Visualizing Kubernetes Resource Relationships with Meshery | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/meshery-visualizing-kubernetes-resource-relationships-with-meshery-pro/xJ9RH0AE7zE.txt
- Transcript chars: 4202
- Keywords: relationships, models, infrastructure, evaluation, inside, resource, hundred, anyway, custom, extensions, visualize, meshery, projects, couple, native, management, extensible, anything

### Resumo baseado na transcript

hey welcome hey my name is Lee calote I am going to talk to you about meshy that fine gentleman just got done pointing out the list of the highest velocity cncf projects well mhy isn't quite where open fpga or open fga open fga is but m is at ninth ninth place out of a couple hundred you know so anyway um m is a cloud native management platform it does a lot it has a big road map it's uh still in the sandbox it's up for incubation

### Excerpt da transcript

hey welcome hey my name is Lee calote I am going to talk to you about meshy that fine gentleman just got done pointing out the list of the highest velocity cncf projects well mhy isn't quite where open fpga or open fga open fga is but m is at ninth ninth place out of a couple hundred you know so anyway um m is a cloud native management platform it does a lot it has a big road map it's uh still in the sandbox it's up for incubation Cloud management platforms they can cover all kinds of all manners of evil this is meant to be an ey chart not really meant to be read what you're supposed to sort of tune in on is the idea that there's a bunch of Yellow Boxes m is quite extensible um I'm going to talk about that extensibility in order for meshy to attempt to help you manage anything Cloud native anything that runs Under the kubernetes Sun or some things that run outside of it some cloud services from some popular providers that offer up integration with their cloud services through kubernetes operators through custom resource definitions M really Keys into that and this is a well a snapshot of sort of each of the projects or each of the operators and custom resources that mesher ties into so for each one of these mesher has a model I'm going to talk more about models before that I'll say meas is quite extensible if I didn't mention that earlier so mry has a growing list of extensions we're going to take a look at one one of them helps you visualize your infrastructure we're going to look at that one before we do we're going to go back to models M has this uh well this idea that if you want to for M to understand your infrastructure help you is it just me or is there an echo it's okay all right okay it's me but okay good measy helps you characterize your infrastructure in very specific way very detailed way the better the crd the better the kubernetes custom resource definition the more in a more detailed way measy can model that infrastructure so every night mes as a project goes out and digests from a couple hundred repos and from artifact Hub thank you artifact Hub uh all the crds that it can find pulls them in and puts them into into individual models um M helps you these models you can package in things like relationships how individual components how a a kubernetes pod relates to a kubernetes service for example there's a relationship that describes that so we were talking about so um so we refer to this as context to wear design there is a an evaluation en
