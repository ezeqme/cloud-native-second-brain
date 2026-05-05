---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Steve Kriss", "Nigel Brown", "VMware"]
sched_url: https://kccnceu2023.sched.com/event/1HySl/contour-the-past-present-and-future-of-the-project-and-community-steve-kriss-nigel-brown-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Contour%3A+The+Past%2C+Present%2C+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Contour: The Past, Present, and Future of the Project and Community - Steve Kriss & Nigel Brown, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Steve Kriss, Nigel Brown, VMware
- Schedule: https://kccnceu2023.sched.com/event/1HySl/contour-the-past-present-and-future-of-the-project-and-community-steve-kriss-nigel-brown-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Contour%3A+The+Past%2C+Present%2C+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Contour: The Past, Present, and Future of the Project and Community.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HySl/contour-the-past-present-and-future-of-the-project-and-community-steve-kriss-nigel-brown-vmware
- YouTube search: https://www.youtube.com/results?search_query=Contour%3A+The+Past%2C+Present%2C+and+Future+of+the+Project+and+Community+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CULmLc5CV6Q
- YouTube title: Contour: The Past, Present, and Future of the Project and Community - Steve Kriss & Nigel Brown
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/contour-the-past-present-and-future-of-the-project-and-community/CULmLc5CV6Q.txt
- Transcript chars: 27080
- Keywords: contour, envoy, support, features, release, external, gateway, virtual, around, implementation, configuration, networking, ingress, coming, cluster, design, involved, routing

### Resumo baseado na transcript

okay hi everyone Thanks for uh joining our Contour project update um let's do a couple of quick intros so my name is Steve Chris I'm a Staff engineer at VMware and I'm a contour maintainer my name is Nigel I am a senior developer Advocate at Intuit and Community manager for Contour uh so what is Contour it's an open source Ingress controller it's a control plane for Envoy how many of you all have used Contour before cool if you've used contour and you don't work at VMware

### Excerpt da transcript

okay hi everyone Thanks for uh joining our Contour project update um let's do a couple of quick intros so my name is Steve Chris I'm a Staff engineer at VMware and I'm a contour maintainer my name is Nigel I am a senior developer Advocate at Intuit and Community manager for Contour uh so what is Contour it's an open source Ingress controller it's a control plane for Envoy how many of you all have used Contour before cool if you've used contour and you don't work at VMware it's like let me oh sick all right cool um uh for those of you who are not familiar with what Contour does what Ingress does in short it helps you get traffic from out into the world uh from in the world into your kubernetes clusters it's not a new project it's been incubating here with the cncf since 2020 and it is currently used in production at scale at VMware and many other places so it supports HTTP proxy the crd that was introduced by this project as well as uh Ingress and the Gateway API as that grows oh yeah a little bit about where it came from yeah so let's let's take a quick look at the timeline of the project so um the project was first open sourced out of heptio back in 2017 so uh coming up on six years ago um 2019 the uh V1 of the project was released and this included um a V1 of the HTTP proxy crd um 2020 was when we're we were donated to the cncf at the incubating level so we've been a cncf project for uh for three years now um 2021 we had the the first Contour release with Gateway API support So Contour maintainers have been involved in in the Gateway API project since the Inception of that project and actually one of our Emeritus maintainers Nick Young was a Founder co-founder of Gateway API so um yeah 2021 our first release with Gateway API support and we've we've continued to develop that through today later in 2021 we moved to uh from a monthly release cycle to a quarterly release cycle so new releases every three months we also moved to supporting the the previous three minor releases so each minor release series now gets nine months of support which includes critical bug fixes and cve fixes um and then fast forward to today so coming up in in just another week or two in early May we're going to have uh V 1.25 out and that will include a bunch of new features that we'll look at uh in a few minutes so yeah let's take a take a look at the kind of the typical deployment architecture for Contour um so Contour uh is an in cluster Ingress controller it's deployed into your
