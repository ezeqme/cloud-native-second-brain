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
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Charles-Edouard Breteche", "Nirmata", "Lanting Chiang", "Karen Tu", "Robinhood Markets", "Inc."]
sched_url: https://kccncna2024.sched.com/event/1hox5/elevate-your-kubernetes-policy-game-with-kyverno-charles-edouard-breteche-nirmata-lanting-chiang-karen-tu-robinhood-markets-inc
youtube_search_url: https://www.youtube.com/results?search_query=Elevate+Your+Kubernetes+Policy+Game+with+Kyverno%21+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Elevate Your Kubernetes Policy Game with Kyverno! - Charles-Edouard Breteche, Nirmata; Lanting Chiang & Karen Tu, Robinhood Markets, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Charles-Edouard Breteche, Nirmata, Lanting Chiang, Karen Tu, Robinhood Markets, Inc.
- Schedule: https://kccncna2024.sched.com/event/1hox5/elevate-your-kubernetes-policy-game-with-kyverno-charles-edouard-breteche-nirmata-lanting-chiang-karen-tu-robinhood-markets-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Elevate+Your+Kubernetes+Policy+Game+with+Kyverno%21+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Elevate Your Kubernetes Policy Game with Kyverno!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hox5/elevate-your-kubernetes-policy-game-with-kyverno-charles-edouard-breteche-nirmata-lanting-chiang-karen-tu-robinhood-markets-inc
- YouTube search: https://www.youtube.com/results?search_query=Elevate+Your+Kubernetes+Policy+Game+with+Kyverno%21+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CuW9Hszlnis
- YouTube title: Elevate Your Kubernetes Policy Game with Kyverno! - C. Breteche, L. Chiang, K. Tu
- Match score: 0.873
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/elevate-your-kubernetes-policy-game-with-kyverno/CuW9Hszlnis.txt
- Transcript chars: 27075
- Keywords: server, policy, report, admission, policies, cluster, reports, actually, storage, security, resources, resource, write, having, pretty, testing, clusters, in-house

### Resumo baseado na transcript

hello everyone thanks for being there today um this session is part of the K MERS track we will explore some real world Integrations and recent cutting Cutting Edge updates so first up let's do a quick round of introductions I'm Char BR ker working at near mat and working exclusively on KERO and open source project project um with me are my fantastic co-p speakers so Karen and lanting can you tell us a word about you uh hi everyone I'm lanting I work on the container orchestration team

### Excerpt da transcript

hello everyone thanks for being there today um this session is part of the K MERS track we will explore some real world Integrations and recent cutting Cutting Edge updates so first up let's do a quick round of introductions I'm Char BR ker working at near mat and working exclusively on KERO and open source project project um with me are my fantastic co-p speakers so Karen and lanting can you tell us a word about you uh hi everyone I'm lanting I work on the container orchestration team of Robin Hood and hello I'm Karen um lanting and I work together to integrate cero into Robin Hood stack awesome today lenting and Karen will kick things off by sharing their experience integrating KERO into their platform uh after that I lead us to a deep dive into kerno reporting system and highlight the latest improvements so let's get started Karen can you start and present the agenda okay so just a quick overview of what we're actually going to talk about so lanting and I will start off with discussing why we actually decided to choose cerno out of all the options that we had and then the process that we follow to actually install cerno and do some of um the migrations and also talk about the strategy for storing policies as code and then we will pass it off to Charles to talk about one of the new features in Cabo okay so I'm going to start off with a little bit of context so um for those of you that don't know Robin Hood is a brokerage firm so there are quite strict security and comp requirements which makes um strong policy enforcement capabilities essential in our kubernetes clusters and this is kind of a slide that represents the state of the world before we installed cerno so we had um pod security policies that we used which um was a part of um kubernetes I say was um because it is actually um removed in the most recent versions um but we were using pod security policies to enforce things like whether a pod could use um the host Network for example and then the next um part of kubernetes um Native that we used is um arbac just for managing um permissions to different resources so this is just through things like cluster roles and cluster rle bindings and finally for the things that native um PSPs and arbac couldn't cover we used our in-house admission server so this is just um a deployment of um a admission server running as go code with go code and um in combination with a web hook configuration and we can write like arbitrary policies using that so I'm going to
