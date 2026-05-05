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
themes: ["Networking"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9c/accelerating-adoption-whats-new-in-envoy-gateway-and-why-it-matters-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Accelerating+Adoption%3A+What%E2%80%99s+New+in+Envoy+Gateway+and+Why+It+Matters+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Accelerating Adoption: What’s New in Envoy Gateway and Why It Matters | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9c/accelerating-adoption-whats-new-in-envoy-gateway-and-why-it-matters-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Accelerating+Adoption%3A+What%E2%80%99s+New+in+Envoy+Gateway+and+Why+It+Matters+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Accelerating Adoption: What’s New in Envoy Gateway and Why It Matters | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9c/accelerating-adoption-whats-new-in-envoy-gateway-and-why-it-matters-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Accelerating+Adoption%3A+What%E2%80%99s+New+in+Envoy+Gateway+and+Why+It+Matters+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=y6O220qbmXc
- YouTube title: Accelerating Adoption: What’s New in Envoy Gateway and Why It Matters | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/accelerating-adoption-whats-new-in-envoy-gateway-and-why-it-matters-pr/y6O220qbmXc.txt
- Transcript chars: 3658
- Keywords: gateway, seeing, policy, releases, envoy, maintainers, november, support, released, active, request, authorization, clients, custom, external, processing, platforms, deploy

### Resumo baseado na transcript

well good afternoon everyone my name is Arco uh I'm an engineer at tet trade and one of the maintainers on the EnV Gateway project uh and today we'll talk about what's new in the project the last time we met was in cucon EU in March we had just G8 with 1.0 uh since then we've been releasing every quarter with 1.1 in July and 1.2 in November uh we've been following the same release Cadence as on by proxy and we lag by lag by about 2 weeks

### Excerpt da transcript

well good afternoon everyone my name is Arco uh I'm an engineer at tet trade and one of the maintainers on the EnV Gateway project uh and today we'll talk about what's new in the project the last time we met was in cucon EU in March we had just G8 with 1.0 uh since then we've been releasing every quarter with 1.1 in July and 1.2 in November uh we've been following the same release Cadence as on by proxy and we lag by lag by about 2 weeks uh the support policy for each of these releases um is 6 months so we've also released patch fixes uh for bugs and CV fixes uh in these last two releases we've released a lot of features some fit on the slide and many that didn't I'll highlight my top five um active passive failover that lets you route to a fallback back end only when the active back end is unhealthy uh request authorization that lets you decide which uh request to accept based on the client IP or the jot claims and Scopes Standalone mode that lets you run on by gatein on VI proxy on the Linux host outside kubernetes a response overrides which lets you standardize your error responses for apis for your clients and Envoy extension policy that lets you run Custom Custom logic uh that doesn't live in onv proxy using uh wasum module or um external processing service our first few adopters were uh users building brand new Greenfield uh platforms but with the last two releases we're seeing a lot of users migrate to on Gateway for their Brownfield platforms as well here are some stats to validate that um Helm seems to be the most common way to consume on by Gateway um users can deploy these starts directly using the helm CLI um or also using CD tools like Argo CD um this graph taken from dockerhub where our charts live showed that our pulls monthly pulls increase from 7,000 last October last November to 64,000 this October we're also seeing an increase in um slack conversations uh 2,000 uh daily visits on GitHub over 700 GitHub issues created uh signaling to us that more users are using on Gateway uh let's look at the ecosystem so we're also seeing many cncf projects integrated on by Gateway for their Ingress solution quadrant a new cncf Sandbox project uh that adds additional uh policies like DNS policy um and O policy on top of Gateway API has recently added native support for on by Gateway K native the serverless platform is integrating with Gateway API and it's added on by Gateway into its conformance testing Suite in the world of geni we're seeing two use ca
