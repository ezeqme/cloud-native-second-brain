---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Charles-Edouard Brétéché", "Mariam Fahmy", "Nirmata", "Raúl Garcia Sanchez", "DE-CIX"]
sched_url: https://kccnceu2024.sched.com/event/1Yhj3/from-chaos-to-control-cloud-native-governance-with-kyverno-charles-edouard-breteche-mariam-fahmy-nirmata-raul-garcia-sanchez-de-cix
youtube_search_url: https://www.youtube.com/results?search_query=From+Chaos+to+Control%3A+Cloud+Native+Governance+with+Kyverno%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# From Chaos to Control: Cloud Native Governance with Kyverno! - Charles-Edouard Brétéché & Mariam Fahmy, Nirmata; Raúl Garcia Sanchez, DE-CIX

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Charles-Edouard Brétéché, Mariam Fahmy, Nirmata, Raúl Garcia Sanchez, DE-CIX
- Schedule: https://kccnceu2024.sched.com/event/1Yhj3/from-chaos-to-control-cloud-native-governance-with-kyverno-charles-edouard-breteche-mariam-fahmy-nirmata-raul-garcia-sanchez-de-cix
- Busca YouTube: https://www.youtube.com/results?search_query=From+Chaos+to+Control%3A+Cloud+Native+Governance+with+Kyverno%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre From Chaos to Control: Cloud Native Governance with Kyverno!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhj3/from-chaos-to-control-cloud-native-governance-with-kyverno-charles-edouard-breteche-mariam-fahmy-nirmata-raul-garcia-sanchez-de-cix
- YouTube search: https://www.youtube.com/results?search_query=From+Chaos+to+Control%3A+Cloud+Native+Governance+with+Kyverno%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-E9bDYYknCI
- YouTube title: From Chaos to Control: Cloud Native Governance with Kyverno!
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/from-chaos-to-control-cloud-native-governance-with-kyverno/-E9bDYYknCI.txt
- Transcript chars: 26473
- Keywords: policy, policies, deployment, admission, validating, resources, basically, replica, deployments, cluster, resource, server, definition, object, controller, binding, clusters, create

### Resumo baseado na transcript

thanks for coming uh thanks for coming thanks for your effort I appreciate that you came to probably one of the last session of this ccon Paris uh please be indulgent it's not easy to pass Friday at 400 p.m. uh we're all tired I hope you won't be sleeping during the presentation H I hope I won't be sleeping too so we are on stage we're going to talk about using Keo to control um and apply policies in Cloud narrative projects uh using

### Excerpt da transcript

thanks for coming uh thanks for coming thanks for your effort I appreciate that you came to probably one of the last session of this ccon Paris uh please be indulgent it's not easy to pass Friday at 400 p.m. uh we're all tired I hope you won't be sleeping during the presentation H I hope I won't be sleeping too so we are on stage we're going to talk about using Keo to control um and apply policies in Cloud narrative projects uh using kop policies rul is going to start and Mariam will talk about uh recent additions in KERO and I will talk about the future of KERO what happened during the past year and how K could change in the next version so R yeah thank you all right so hi everyone my name is R Garcia I work for the diix one of the biggest uh internet Exchange in Germany and um yeah before we start with that uh let me quickly introduce uh who diig is and and uh also show you about how the environment is looking exactly before we then move over how we have implemented keano and why exactly so diix is one of the leading operators of ips in the world to facilitate the interconnection of networks so that we make uh improvements into the efficiency of Internet services globally we offer a lot of different services like uh for peering or other interconnections like Cloud connects so the um yeah we basically play a crucial role in thank you a crucial role in the internet architecture for Network providers CDN uh large Enterprise networks so that yeah all of these networks exchange traffic directly um so that basically we reduce latency increase bandwidth and uh yeah increase the reliability on the internet uh here on this map you can basically see where we are present and where you can basically interconnect with us how is the environment looking so we basically have an application platform team which um yeah is providing centralized services like a monitoring a long-term metric storage a logging stack uh we also provide oci image registry we have a secret store codre pository and so on so basically we try to provide a holistic stack for all the teams and then we have different teams that get manage kubernetes clusters they get a monitoring stack they get a logging environment that we take care of we provide them with incest controller with Secret store access and so on and so forth but all in a way that they still are able to do selfservice so we want the teams to create their deployments by themselves to use kubernetes techniques and um yeah all of this howeve
