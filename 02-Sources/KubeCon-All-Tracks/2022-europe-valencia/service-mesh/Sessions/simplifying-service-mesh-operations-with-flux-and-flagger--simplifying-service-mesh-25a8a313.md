---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Service Mesh"
themes: ["Networking", "GitOps Delivery"]
speakers: ["Mitch Connors", "Google", "Stefan Prodan", "Weaveworks"]
sched_url: https://kccnceu2022.sched.com/event/ytt9/simplifying-service-mesh-operations-with-flux-and-flagger-mitch-connors-google-stefan-prodan-weaveworks
youtube_search_url: https://www.youtube.com/results?search_query=Simplifying+Service+Mesh+Operations+with+Flux+and+Flagger+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Simplifying Service Mesh Operations with Flux and Flagger - Mitch Connors, Google & Stefan Prodan, Weaveworks

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]], [[GitOps Delivery]]
- País/cidade: Spain / Valencia
- Speakers: Mitch Connors, Google, Stefan Prodan, Weaveworks
- Schedule: https://kccnceu2022.sched.com/event/ytt9/simplifying-service-mesh-operations-with-flux-and-flagger-mitch-connors-google-stefan-prodan-weaveworks
- Busca YouTube: https://www.youtube.com/results?search_query=Simplifying+Service+Mesh+Operations+with+Flux+and+Flagger+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Simplifying Service Mesh Operations with Flux and Flagger.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytt9/simplifying-service-mesh-operations-with-flux-and-flagger-mitch-connors-google-stefan-prodan-weaveworks
- YouTube search: https://www.youtube.com/results?search_query=Simplifying+Service+Mesh+Operations+with+Flux+and+Flagger+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1rJYsdLgJGA
- YouTube title: Simplifying Service Mesh Operations with Flux and Flagger - Mitch Connors & Stefan Prodan
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/simplifying-service-mesh-operations-with-flux-and-flagger/1rJYsdLgJGA.txt
- Transcript chars: 32087
- Keywords: istio, flux, cluster, upgrade, version, control, flagger, running, actually, release, request, upgrades, production, deployment, github, stefan, mesh, little

### Resumo baseado na transcript

thanks daniel well as daniel said my name is mitch connors i've been a software engineer at google on the istio project for three and a half years hello everyone i'm stefan pradhan i'm a principal engineer at weworks and i'm on flux and flagger maintainers for many years all right well let's get to it everyone here should probably already know that istio makes your service mesh more secure right it's the leading reason for adoption among our users they want the security they want zero trust built on our traffic going to the old version and it's going to periodically check with prometheus and ask is the service still healthy shift a little bit more is the service still healthy shift a little bit more and it's going to be really boring which we want to without like patch updates can roll out without a pull request or they could be stuck with a pull request it just depends on how your operational like security and safety how much how paranoid you want to be i want to

### Excerpt da transcript

thanks daniel well as daniel said my name is mitch connors i've been a software engineer at google on the istio project for three and a half years hello everyone i'm stefan pradhan i'm a principal engineer at weworks and i'm on flux and flagger maintainers for many years all right well let's get to it everyone here should probably already know that istio makes your service mesh more secure right it's the leading reason for adoption among our users they want the security they want zero trust built on mtls they want the ability to set authen and off z policies to have their certificates automatically rotated and it makes all of that really easy and seamless but there's a little bit of a catch of istio installations are running known cves so if you're using istio to make your service mesh more secure and then istio that you're running has its own cves some of them 9 9.8 on the cve scale that that's problematic in fact your service mesh could be less secure because istio is there rather than more secure so why is this why are 88 it's not that istio is not patching their vulnerabilities right we have patch releases that come out at least once a month each of them covers a bunch of known cves uh but it's still not being picked up in the community very quickly so today we're going to talk just for a brief time about why our users aren't upgrading i'm going to rely on stefan a lot to tell us how good ops can help us with this problem we'll have actually a handful of demos sprinkled throughout and some takeaways so this is sort of a timeline a history of what we thought was the problem with upgrades in the istio project and as you can see it's changed a lot over time we first noticed that no one was upgrading istio in q2 of 2020 and we thought well maybe they don't know maybe users don't realize that there are cves in their istio installation so we ran a survey and we did find a few users who were unaware and we built some tooling and some documentation to help boost that awareness we found a lot more users who were aware that their service mesh was vulnerable but they didn't feel like they had time to get to it you know these istio is not the only thing that anyone is running in production they've got their own apps they've got telemetry systems they've got maybe some ebpf systems that need to stay up to date and staying on top of all of it is just so difficult it's like a treadmill that you can never keep up with so we decided let's make istio upgrades easier thi
