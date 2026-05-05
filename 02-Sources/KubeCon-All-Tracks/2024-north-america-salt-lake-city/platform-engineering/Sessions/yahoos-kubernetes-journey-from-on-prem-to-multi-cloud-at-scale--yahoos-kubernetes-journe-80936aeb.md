---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core", "SRE Reliability"]
speakers: ["Nandhakumar Venkatachalam", "Payal Patel", "Yahoo"]
sched_url: https://kccncna2024.sched.com/event/1i7rf/yahoos-kubernetes-journey-from-on-prem-to-multi-cloud-at-scale-nandhakumar-venkatachalam-payal-patel-yahoo
youtube_search_url: https://www.youtube.com/results?search_query=Yahoo%E2%80%99s+Kubernetes+Journey+from+on-Prem+to+Multi-Cloud+at+Scale+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Yahoo’s Kubernetes Journey from on-Prem to Multi-Cloud at Scale - Nandhakumar Venkatachalam & Payal Patel, Yahoo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Nandhakumar Venkatachalam, Payal Patel, Yahoo
- Schedule: https://kccncna2024.sched.com/event/1i7rf/yahoos-kubernetes-journey-from-on-prem-to-multi-cloud-at-scale-nandhakumar-venkatachalam-payal-patel-yahoo
- Busca YouTube: https://www.youtube.com/results?search_query=Yahoo%E2%80%99s+Kubernetes+Journey+from+on-Prem+to+Multi-Cloud+at+Scale+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Yahoo’s Kubernetes Journey from on-Prem to Multi-Cloud at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rf/yahoos-kubernetes-journey-from-on-prem-to-multi-cloud-at-scale-nandhakumar-venkatachalam-payal-patel-yahoo
- YouTube search: https://www.youtube.com/results?search_query=Yahoo%E2%80%99s+Kubernetes+Journey+from+on-Prem+to+Multi-Cloud+at+Scale+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vySVIZuLRcg
- YouTube title: Yahoo’s Kubernetes Journey from on-Prem to Multi-Cloud at Scale - N. Venkatachalam, P. Patel
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/yahoos-kubernetes-journey-from-on-prem-to-multi-cloud-at-scale/vySVIZuLRcg.txt
- Transcript chars: 31165
- Keywords: cluster, infrastructure, version, create, upgrade, application, provide, network, meaning, interface, started, clusters, journey, platform, source, control, leverage, policy

### Resumo baseado na transcript

good morning everyone welcome to the talk it is fantastic to be speaking at the cubec con once again in front of the awesome audience my name is nandakumar wenar aalam I'm a senior principal engineer at yahu today I have my colleague P Patel with me over the past 17 and a half years I have had the incredible opportunity to work on various projects at yahu one of the groundbreaking projects that particularly exciting is the work we did with the kubernetes today we thrilled to share our

### Excerpt da transcript

good morning everyone welcome to the talk it is fantastic to be speaking at the cubec con once again in front of the awesome audience my name is nandakumar wenar aalam I'm a senior principal engineer at yahu today I have my colleague P Patel with me over the past 17 and a half years I have had the incredible opportunity to work on various projects at yahu one of the groundbreaking projects that particularly exciting is the work we did with the kubernetes today we thrilled to share our platform Journey with all of you here's the quick agenda for the talk we'll be talking about the user interface on from adventures and the digital transformation Journey let me share some quick history of how it all started and the challenges inspired us to build this platform looking at the tech landscape of 2016 especially most of our deployments were in bare metal it took a long time to launch a new product especially it involved capital expenditure and took a long time to set up application infrastructure there were a lot of duplications there were effort to containerize the workload specifically finding the right container orchestration platform there were misos and kubernetes and you know kubernetes stood out for the simplicity building on to the success with the kubernetes it was very clear that Yahoo needed a robust and scalable infrastructure to host its wor array of services it's not just the kuber Simplicity its portability would allow one to deploy to multiple clouds including on Prem so this versatility laid the foundation for our platform team which we named Omega I know it sounds crazy it's a precursor to the kubernetes so we have core principles that led success to our platform team it's one team Focus everything on kubernetes solve common problems affecting many teams we built lightweight set of tools and templates to make it straightforward for someone to deploy application onto the kubernetes by means we take care of common nties of the use cases things like application identity and the security and the networking whatnot one of the key aspect of our platform is that the full kubernetes interface is still available to the users this is to empower the advanced users to make use of full of the kubernetes ecosystem we heard a lot about the abstraction but we believe that abstraction helps eliminate the complexity especially 2016 we didn't want to let thousands of developers to figure out how to deploy onto the kubernetes it was pretty new at that time so our t
