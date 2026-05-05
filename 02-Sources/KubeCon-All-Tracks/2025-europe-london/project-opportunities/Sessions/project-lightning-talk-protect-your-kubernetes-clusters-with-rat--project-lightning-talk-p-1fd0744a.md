---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Kubernetes Core", "Community Governance"]
speakers: ["Yi Zha", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcv8/project-lightning-talk-protect-your-kubernetes-clusters-with-ratify-and-attestations-yi-zha-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Protect+your+Kubernetes+Clusters+with+Ratify+and+Attestations+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Protect your Kubernetes Clusters with Ratify and Attestations - Yi Zha, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Yi Zha, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcv8/project-lightning-talk-protect-your-kubernetes-clusters-with-ratify-and-attestations-yi-zha-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Protect+your+Kubernetes+Clusters+with+Ratify+and+Attestations+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Protect your Kubernetes Clusters with Ratify and Attestations.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcv8/project-lightning-talk-protect-your-kubernetes-clusters-with-ratify-and-attestations-yi-zha-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Protect+your+Kubernetes+Clusters+with+Ratify+and+Attestations+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lNovu7Kclhk
- YouTube title: Project Lightning Talk: Protect your Kubernetes Clusters with Ratify and Attestations - Yi Zha
- Match score: 1.04
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-protect-your-kubernetes-clusters-with-ratify-an/lNovu7Kclhk.txt
- Transcript chars: 4409
- Keywords: ratify, signature, report, scenario, images, policies, vulnerability, attestations, validate, signed, whether, statement, notary, supply, supports, cosign, currently, language

### Resumo baseado na transcript

So I'm now switching the role from notary project maintainer to ratify maintainer. So today I will give you a brief uh overview of ratify project and uh uh a bit deep dive into attachations. So you can basically set up those policies based on your company's security and compliance uh policies and you can also scan the QR to know more on from the not uh from the ratify project website. To learn more uh welcome to join our uh project Koski uh it happens tomorrow.

### Excerpt da transcript

Hi me me again. Uh my name is E. So I'm now switching the role from notary project maintainer to ratify maintainer. So today I will give you a brief uh overview of ratify project and uh uh a bit deep dive into attachations. So what is ratify? Ratify is a sandbox project. uh it has been around uh uh less less than one year I think it's uh have been donated uh uh last year um I think uh if I remember correctly it's in September so Ratify is a pluggable verific um verification engine to safeguard the cloud native secure supply chain and it supports uh signature uh not project signature and uh cosign signature uh cosign for cosign signature it includes the k signature and the kitty's signature and it supports currently uh the artifact tab spawn uh vulnerability report in uh uh and also the attestations uh the policy language it supports reggo language and we have the plan to support language and ratify also compliance with OSI 1.1 so it can pull uh the OSI artifacts uh efficiently. So currently we have uh also uh major cloud uh vendors adopt the ratify.

So uh three key scenarios for uh ratify. The first one is ratify can uh used as external data provider integrated with uh gatekeeper op gatekeeper for uh policy control. Uh so this normally happening uh in when you want to deploy uh workloads uh on kubernetes. So ratify can work with uh gatekeeper to set up policies to write data signatures spawn files and attestations. The second scenario is uh uh roify um integrate with the containerd at runtime. So for this scenario it's uh um uh happened uh in in the scenario you want to validate the signature uh or you want to verify the container images on a node level. So for example if you uh want to uh bootstrap a kubernetes cluster. So at that time the admission controller the first scenario it is not ready yet but you have some cached images and you want to make sure those images can be trusted. So this is the scenar scenario two uh can be used for that purpose for uh scenario two currently is in a proof of concept stage for uh the third scenario is to use ratify in the CI/CD system so that you can not only uh validate the signatures but also you can uh enforce policies for validate other uh supply chain related artifacts such as spawn vulnerability reports So a bit deep dive into attachations.

So attestations is a statement. It's a signed statement. So the statement could be a spawn uh or could be a vulnerability report and this statement uh is signed to ensure it
