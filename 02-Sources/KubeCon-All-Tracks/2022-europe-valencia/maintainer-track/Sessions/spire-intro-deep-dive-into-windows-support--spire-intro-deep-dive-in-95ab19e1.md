---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Agustín Martínez Fayó", "Marcos Yacob", "Hewlett Packard Enterprise"]
sched_url: https://kccnceu2022.sched.com/event/yttL/spire-intro-deep-dive-into-windows-support-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
youtube_search_url: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+Deep+Dive+Into+Windows+Support+CNCF+KubeCon+2022
slides: []
status: parsed
---

# SPIRE: Intro & Deep Dive Into Windows Support - Agustín Martínez Fayó & Marcos Yacob, Hewlett Packard Enterprise

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Agustín Martínez Fayó, Marcos Yacob, Hewlett Packard Enterprise
- Schedule: https://kccnceu2022.sched.com/event/yttL/spire-intro-deep-dive-into-windows-support-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
- Busca YouTube: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+Deep+Dive+Into+Windows+Support+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre SPIRE: Intro & Deep Dive Into Windows Support.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/yttL/spire-intro-deep-dive-into-windows-support-agustin-martinez-fayo-marcos-yacob-hewlett-packard-enterprise
- YouTube search: https://www.youtube.com/results?search_query=SPIRE%3A+Intro+%26+Deep+Dive+Into+Windows+Support+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pcyOnX08jHs
- YouTube title: SPIRE: Intro & Deep Dive Into Windows Support - Agustín Martínez Fayó & Marcos Yacob
- Match score: 0.792
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/spire-intro-deep-dive-into-windows-support/pcyOnX08jHs.txt
- Transcript chars: 20613
- Keywords: windows, server, running, docker, inspire, identity, domain, workload, entries, selectors, products, process, workloads, information, customer, aspire, little, provide

### Resumo baseado na transcript

thank you for joining us today uh in this session we will talk about spider my name is austin martini fasho i am part of the hpe security engineering team and i am maintainer of the inspire project i'm here with marcos okay hello i'm marcos i am working on hp security engineering team two and i am an editor of the maintainer of aspire okay um so we will be providing an introduction of aspire and also we will be doing a deep dive into the the new window all these services to be able to test we need we need yes entries so i will create them for this demo in total we have three entries one is for our web app that has aspirin id the spf id of the agent which

### Excerpt da transcript

thank you for joining us today uh in this session we will talk about spider my name is austin martini fasho i am part of the hpe security engineering team and i am maintainer of the inspire project i'm here with marcos okay hello i'm marcos i am working on hp security engineering team two and i am an editor of the maintainer of aspire okay um so we will be providing an introduction of aspire and also we will be doing a deep dive into the the new window support that we just released um so uh we will do an introduction to inspire uh in order to do that uh we will first talk about uh spiffy we will do a quick overview of spf then we will look into the basic component of the spire architecture we will talk a little bit about the adoption of spire and then we will start talking about the new windows support we will see what are the difference between running expire on windows and on linux we will see how the development experience looks like and finally we will see a demo of spire running on windows this is the first time that we will see spy running on windows in a conference so looking forward to that okay uh so let's start talking about spiffy spf is a set of open source standards that they all share the same common goals that is to able to be able to securely identify workloads no matter where they are running in order to do that we need to represent an id or to provide ids and for that we have the spf id that is a representation of an identity we can see that uh this is how spf id looks like it is a uri that has the spf scheme the authority component is what we call a trust domain a trust domain in spf defines security boundaries so if one trust domain is compromised that shouldn't affect a different trust domain and you may run a trust domain for development for example and a different trust domain for production that will set the boundaries there and finally the path part of a spf id of this uri identifies a specific workflow within a trust domain so but spf is not only about spf ids we also need some kind of document or place where we can actually put that id and be able to verify it and for that the spf standards define what we call a spiffy verifiable identity document or svit and we can think of an asset like a passport in the same way that in a passport you have your identity there and there is a way that you the identity can be verified in an svid you have the spf id that is the identity and also you can it is cryptographically verifiable so that's
