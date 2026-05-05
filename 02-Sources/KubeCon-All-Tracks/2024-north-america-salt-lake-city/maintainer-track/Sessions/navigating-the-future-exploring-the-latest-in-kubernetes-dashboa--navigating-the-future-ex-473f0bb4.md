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
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Marcin Maciaszczyk", "Sebastian Florek", "Plural"]
sched_url: https://kccncna2024.sched.com/event/1hoym/navigating-the-future-exploring-the-latest-in-kubernetes-dashboard-development-marcin-maciaszczyk-sebastian-florek-plural
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+the+Future%3A+Exploring+the+Latest+in+Kubernetes+Dashboard+Development+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Navigating the Future: Exploring the Latest in Kubernetes Dashboard Development - Marcin Maciaszczyk & Sebastian Florek, Plural

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Marcin Maciaszczyk, Sebastian Florek, Plural
- Schedule: https://kccncna2024.sched.com/event/1hoym/navigating-the-future-exploring-the-latest-in-kubernetes-dashboard-development-marcin-maciaszczyk-sebastian-florek-plural
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+the+Future%3A+Exploring+the+Latest+in+Kubernetes+Dashboard+Development+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Navigating the Future: Exploring the Latest in Kubernetes Dashboard Development.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoym/navigating-the-future-exploring-the-latest-in-kubernetes-dashboard-development-marcin-maciaszczyk-sebastian-florek-plural
- YouTube search: https://www.youtube.com/results?search_query=Navigating+the+Future%3A+Exploring+the+Latest+in+Kubernetes+Dashboard+Development+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7BV1QAgTCxI
- YouTube title: Navigating the Future: Exploring the Latest in Kubernetes Dashboard Dev... M. Maciaszczyk, S. Florek
- Match score: 0.934
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/navigating-the-future-exploring-the-latest-in-kubernetes-dashboard-dev/7BV1QAgTCxI.txt
- Transcript chars: 13715
- Keywords: basically, dashboard, support, resource, server, cluster, actually, request, already, multicluster, changes, architecture, gateway, thanks, return, future, moment, previously

### Resumo baseado na transcript

so to introduce ourselves I'm Martin I'm working on kubernetes dashboard project since uh basically the very beginning um yeah at the moment um I'm one of the CI co-leaders um yeah and I'm Sebastian uh I'm also working basically from the beginning on the project and I am currently software engineer at uh plural and also one of the co-leaders in this UI and yeah our our agenda for today is basically do the the project background so very short one um key changes so the new architecture that

### Excerpt da transcript

so to introduce ourselves I'm Martin I'm working on kubernetes dashboard project since uh basically the very beginning um yeah at the moment um I'm one of the CI co-leaders um yeah and I'm Sebastian uh I'm also working basically from the beginning on the project and I am currently software engineer at uh plural and also one of the co-leaders in this UI and yeah our our agenda for today is basically do the the project background so very short one um key changes so the new architecture that we um uh recently adopted um then we will talk about the Standalone API uh so that how we moved it to be like a stand one basically API that we reuse and the resource list cach that we introduced just a couple of weeks ago uh then we'll talk uh shortly about some user experience enhancements and future road map and that maybe some questions if you'll have any um yeah so um to give like short uh project background so kubernetes dashboard is there from around uh 2015 so the first commit was done in 2015 right now we have uh version uh 79.0 which was released uh in October um and it provides support for kubernetes uh version 1.31 um we uh get about like 8 Millions uh image pools uh every month and the number of uh Total Image pools is like really big which is over 1.1 billion um yeah so as Sebastian said uh we wanted to go through uh key changes that we've did uh we have done recently so um this uh like the new architecture we spoke about it um like some time ago but it took actually some time to complete so uh what we did is like previously uh kubernetes dashboard was uh application which was running inside one container and this was uh our API and UI um but uh we have uh splitted it into multiple containers uh that can be reused so the uh the one that can can be most useful is uh our API um yeah so we have a container for UI API we also have metric scraper which was previously hosted uh in kubernetes 6 organization right now it's part of the main uh kubernetes dashboard repository we also have uh authentication container um yeah and as you can see besides all of uh this for containers we also uh our deployment also uh contains uh Gateway at the moment uh it's only temporary we plan to uh plan to update it uh in some time it's it's on our road map um yeah so uh this uh this feature is already completed and it's part of our latest release yeah and the next thing is is um yeah the Standalone API so uh thanks to the changes that we've done and thanks to actually making the API
