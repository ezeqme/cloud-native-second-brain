---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Joe Betz", "Google"]
sched_url: https://kccnceu2021.sched.com/event/iE8f/extend-all-the-things-cloud-provider-edition-joe-betz-google
youtube_search_url: https://www.youtube.com/results?search_query=%22Extend+All+The+Things%21%22%3A+Cloud+Provider+Edition+CNCF+KubeCon+2021
slides: []
status: parsed
---

# "Extend All The Things!": Cloud Provider Edition - Joe Betz, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Joe Betz, Google
- Schedule: https://kccnceu2021.sched.com/event/iE8f/extend-all-the-things-cloud-provider-edition-joe-betz-google
- Busca YouTube: https://www.youtube.com/results?search_query=%22Extend+All+The+Things%21%22%3A+Cloud+Provider+Edition+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre "Extend All The Things!": Cloud Provider Edition.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE8f/extend-all-the-things-cloud-provider-edition-joe-betz-google
- YouTube search: https://www.youtube.com/results?search_query=%22Extend+All+The+Things%21%22%3A+Cloud+Provider+Edition+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kv5zaJ_o3iQ
- YouTube title: "Extend All The Things!": Cloud Provider Edition - Joe Betz, Google
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/extend-all-the-things-cloud-provider-edition/kv5zaJ_o3iQ.txt
- Transcript chars: 23811
- Keywords: provider, controller, controllers, server, control, container, specific, extension, process, running, kubelet, extensibility, providers, cluster, manager, pretty, credentials, talking

### Resumo baseado na transcript

welcome my name is joe batz and today i'm going to be talking about cloud provider integrations with kubernetes and the extensibility features around that a couple things about myself so i'm a std maintainer i've been working at google i've been involved in kubernetes for about four years i'm mostly involved in api machinery i've contributed to bringing custom resource definitions to ga bringing admission web hooks to ga and more recently developing the server side apply feature which is slated to go to ga in the upcoming 1.22

### Excerpt da transcript

welcome my name is joe batz and today i'm going to be talking about cloud provider integrations with kubernetes and the extensibility features around that a couple things about myself so i'm a std maintainer i've been working at google i've been involved in kubernetes for about four years i'm mostly involved in api machinery i've contributed to bringing custom resource definitions to ga bringing admission web hooks to ga and more recently developing the server side apply feature which is slated to go to ga in the upcoming 1.22 release more recently i've gotten involved in sig cloud provider and i'm going to be talking about that quite a bit today i've got a lot to cover i'm still going to start by talking a little bit about the cloud provider extraction project which is a fairly large initiative in the kubernetes community i'm then going to switch gears and focus on kubernetes extensibility features in general and then start to kind of work our way down to the more cloud provider specific extensibility features from there we'll dig into how those features can be used to build cloud provider integrations and help move the cloud provider extraction project forward i'll then finish up by talking a little bit about how this makes kubernetes better both for the kubernetes developers and for the ecosystem at large so let's get started let's start by talking about the cloud provider extraction project this is a project that's led by sig cloud provider and it really comes from their core mission statement which includes the goal of evolving the kubernetes ecosystem in a way that is neutral to all cloud providers to get a sense of what that means let's have a look at the code so on the left here we have a list of the cloud providers that are in the main kubernetes source tree these cloud providers are uh directly combi compiled into the main kubernetes binaries um and are deeply integrated with the kubernetes code base on the right we have the out of tree cloud providers these are cloud providers that are exist in their own separate source repos are built out of their own binaries and only interact with the main kubernetes binaries through extension points you might have already noticed that there's some overlap like some of these cloud dividers are in both right entry and out of tree there's a reason for this there's currently a migration going on to move all entry cloud providers out of tree so these are the source and destinations of that migration when this mig
