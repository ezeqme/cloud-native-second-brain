---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Observability"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Matthias Loibl", "Polar Signals", "Nadine Vehling", "Grafana Labs"]
sched_url: https://kccncna2022.sched.com/event/182G2/slo-based-observability-for-all-kubernetes-cluster-components-matthias-loibl-polar-signals-nadine-vehling-grafana-labs
youtube_search_url: https://www.youtube.com/results?search_query=SLO-Based+Observability+For+All+Kubernetes+Cluster+Components+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SLO-Based Observability For All Kubernetes Cluster Components - Matthias Loibl, Polar Signals & Nadine Vehling, Grafana Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Matthias Loibl, Polar Signals, Nadine Vehling, Grafana Labs
- Schedule: https://kccncna2022.sched.com/event/182G2/slo-based-observability-for-all-kubernetes-cluster-components-matthias-loibl-polar-signals-nadine-vehling-grafana-labs
- Busca YouTube: https://www.youtube.com/results?search_query=SLO-Based+Observability+For+All+Kubernetes+Cluster+Components+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SLO-Based Observability For All Kubernetes Cluster Components.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182G2/slo-based-observability-for-all-kubernetes-cluster-components-matthias-loibl-polar-signals-nadine-vehling-grafana-labs
- YouTube search: https://www.youtube.com/results?search_query=SLO-Based+Observability+For+All+Kubernetes+Cluster+Components+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AC38JtXXE50
- YouTube title: SLO-Based Observability For All Kubernetes Cluster Components - Matthias Loibl & Nadine Vehling
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/slo-based-observability-for-all-kubernetes-cluster-components/AC38JtXXE50.txt
- Transcript chars: 30270
- Keywords: prometheus, actually, slo, requests, budget, metrics, running, objective, latency, amount, cluster, grafana, request, interesting, server, components, availability, alerts

### Resumo baseado na transcript

Perfect all right let's get started so uh I'm Matias LEL um I work at polar signals we do continuous profiling and with me virtually today is Nadine failing she works at grafana Labs as a ux designer and we want to talk to you about SLO based observability for all kubernetes cluster components today uh let's see if all actually had some learnings during making the slides but yeah let's get into it so this kind of what we are trying to do um we have uh all sorts down here so that was fine but yeah we can see we went from 60% error budget to 59 so whatever it shouldn't even alert um and then one other thing I want to look at are core DNS respon l latencies and I don't but and that's kind of sad for the demo it's not too bad so usually if it was bad enough um one or in in some cases even all four of these multi bur rate alerts would would alert you depending on the severity and how quickly so the multi burner alerts alert on how quickly the arrow budget is burning so if you like just burn pretty slow over two weeks and you might like uh end up with like zero aror budget left then that is just a very interesting um and uh how do we envision P being integrated into the workflow of an engineer so do you see me going to Pura after seeing an alert on slack or should I have it on a on a big screen on my

### Excerpt da transcript

Perfect all right let's get started so uh I'm Matias LEL um I work at polar signals we do continuous profiling and with me virtually today is Nadine failing she works at grafana Labs as a ux designer and we want to talk to you about SLO based observability for all kubernetes cluster components today uh let's see if all actually had some learnings during making the slides but yeah let's get into it so this kind of what we are trying to do um we have uh all sorts of of components in a cluster and we want to be able to measure and kind of objectify the uh yeah the the individual components availability targets um so first of all we're going to talk about the fundamentals of slos this is a beginner talk so I want to quickly talk about that before talking about Pura um a bit more and then how to create slos with that uh and obviously look at cluster uh components uh quick demo and then what the future holds so what are slos um imagine you go to the GitHub page of of the project uh there are many uh requests made but let's focus on the initial request um that loads the HTML and you want 99% of these requests to succeeds within 5 minutes um so that's kind of a very U yeah usual uh SLO maybe within one second might actually be what you are uh even more focused on on doing but yeah let's let's say 5 minutes so that's kind of an example and SLI are the underlying often times just metrics um but we use these two to measure uh the amount of errors and successful requests and then compare those against the total amount of requests that our system gets and that already brings us to what availability is so we kind of take the amount of successful requests and divide them by the total amount of requests and we get something like 99.3% of requests are are successful right so like looking at that from from a request based system you also have like batch systems where like um the operations might be um in a in a different way not request based but uh yeah like you would also measure the successful events there against the amount of total uh events and then the more interesting concept on top of that with slos is error budget so let's dive a bit more in detail into that CU I often find it's it's like slightly confusing when starting out so we have always like the 100% And we never get to 100% um if you want to try to achieve 100% good luck kind of impossible over weeks and and months of uh of of time but um let's say you have a 90% objective um and the inverse is always kind
