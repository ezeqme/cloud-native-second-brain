---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Unclassified"
themes: ["AI ML"]
speakers: ["Yury Tsarev", "Upbound", "Nuno Guedes", "Millennium bcp"]
sched_url: https://kccnceu2023.sched.com/event/1HyW3/recovering-from-regional-failures-at-cloud-native-speeds-yury-tsarev-upbound-nuno-guedes-millennium-bcp
youtube_search_url: https://www.youtube.com/results?search_query=Recovering+from+Regional+Failures+at+Cloud+Native+Speeds+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Recovering from Regional Failures at Cloud Native Speeds - Yury Tsarev, Upbound & Nuno Guedes, Millennium bcp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yury Tsarev, Upbound, Nuno Guedes, Millennium bcp
- Schedule: https://kccnceu2023.sched.com/event/1HyW3/recovering-from-regional-failures-at-cloud-native-speeds-yury-tsarev-upbound-nuno-guedes-millennium-bcp
- Busca YouTube: https://www.youtube.com/results?search_query=Recovering+from+Regional+Failures+at+Cloud+Native+Speeds+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Recovering from Regional Failures at Cloud Native Speeds.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyW3/recovering-from-regional-failures-at-cloud-native-speeds-yury-tsarev-upbound-nuno-guedes-millennium-bcp
- YouTube search: https://www.youtube.com/results?search_query=Recovering+from+Regional+Failures+at+Cloud+Native+Speeds+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=U46hlF0Z3xs
- YouTube title: Recovering from Regional Failures at Cloud Native Speeds - Yury Tsarev, Upbound & Nuno Guedes
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/recovering-from-regional-failures-at-cloud-native-speeds/U46hlF0Z3xs.txt
- Transcript chars: 22597
- Keywords: cluster, clusters, global, application, europe, simple, solution, actually, basically, environment, ingress, balancing, standard, strategy, management, amazing, running, single

### Resumo baseado na transcript

all right thanks a lot for joining uh let's chat about surviving the regional fillers so first Speaker slide let me introduce amazing end user of the project we are going to talk about Nuno and creator of KGB Yuri thank you so show of hands whoever heard about KGB is a kubernetes global balancer before amazing much more people than I expected I appreciate it so what is KGB kubernetes Global balancer open source project sandbox one a it is designed to solve the global server load balancing problem

### Excerpt da transcript

all right thanks a lot for joining uh let's chat about surviving the regional fillers so first Speaker slide let me introduce amazing end user of the project we are going to talk about Nuno and creator of KGB Yuri thank you so show of hands whoever heard about KGB is a kubernetes global balancer before amazing much more people than I expected I appreciate it so what is KGB kubernetes Global balancer open source project sandbox one a it is designed to solve the global server load balancing problem and challenge in cloud94 so it is running on top of kubernetes it is designed to be as simple to use as possible it's just reconcile the single crd of jslb type it is it doesn't require any management cluster so that's a strong point of the solution and no incurrent no single point of failure so and design design on top of well battle tested DNS protocol and support some a pretty good set of global load balancing strategies so a little bit of project history in context why it was even created so uh it was originated in Absa and Absa is amazing South African bank I had a honor to work for and they are running I believe still running a huge kubernetes uh Fleet more than 100 clusters and they required some form of jsob solutions that is cloud native so that is aware of kubernetes primitive what is happening down to the podcast level and backing up so we needed geographically a solution that would steer the traffic to geographically disparate clusters and this geography could mean like different data centers on-prem or different regions uh in Edwards cloud or actually a mix of them we try to find some proprietary vendor Solutions there was nothing that was Cloud native enough and uh basically most of the solutions load balancing Global load balancing one they uh relying on a simple simple straightforward HTTP checks and that's it's just not fast enough for cloud94 so that's why we decided to uh build a solution from scratch and it was something that we developed in open from day Zero so it wasn't something that was born internally uh we and then open sourced we were starting it as a OSS project from the very first day and I think it uh very positively positively affected the overall design of the project and we never made any shortcuts so in a nutshell uh how it works right very very simple thing you have at least two clusters that are geographically dispersed you in this specific example on the diagram you have one cluster in European region or data center or another
